from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

if sys.version_info < (3, 0):
  reload(sys)
  sys.setdefaultencoding('utf8')


def parse_rst(filename):
  """Parse R-specific RST files as part of CRAN specs.
  This is a very naive parser for reading RST files specific to R docs.
  The RST file has a Title, followed by Description, Usage, Format, Details,
  Note, Source and References. The sections are optional. This parser
  works for these specific files and may fail for others.

  Args:
    filename: str.
      Path to rst file

  Returns:
    Dictionary of start and end positions of extracted sections from the
    rst file.
  """
  with open(filename) as f:
    title_start = 0
    desc_line_start = 0
    desc_line_end = 0
    format_start = 0
    format_end = 0
    details_start = 0
    details_end = 0
    notes_start = 0
    notes_end = 0
    source_start = 0
    source_end = 0
    final_line = 0
    for i, line in enumerate(f):
      title_start = 4
      if line.strip() == 'Description':
        desc_line_start = i + 2
      if line.strip() == 'Usage':
        desc_line_end = i - 1
      if line.strip() == 'Format':
        if desc_line_end == 0:
          desc_line_end = i - 1
        format_start = i + 2
      if line.strip() == 'Details':
        if desc_line_end == 0:
          desc_line_end = i - 1
        if format_start > 0:
          format_end = i - 1
        details_start = i + 2
      if line.strip() == 'Note':
        if desc_line_end == 0:
          desc_line_end = i - 1
        if format_start > 0:
          format_end = i - 1
        notes_start = i + 2
      if line.strip() == 'Source':
        if desc_line_end == 0:
          desc_line_end = i - 1
        if format_end == 0:
          format_end = i - 1
        if details_start > 0:
          details_end = i - 1
        if notes_start > 0:
          notes_end = i - 1
        source_start = i + 2
      if line.strip() == 'References':
        source_end = i - 1
        if format_end == 0:
          format_end = i - 1
      if line.strip() == 'Examples':
        if source_end == 0:
          source_end = i - 1
        if format_end == 0:
          format_end = i - 1
      final_line = i
    if source_end == 0:
      source_end = final_line
    if format_end == 0:
      format_end = final_line
  extract_dict = {'title': title_start,
                  'desc_start': desc_line_start,
                  'desc_end': desc_line_end,
                  'format_start': format_start,
                  'format_end': format_end,
                  'source_start': source_start,
                  'source_end': source_end,
                  'final_line': final_line,
                  'file_name': filename
                  }
  for k, v in extract_dict.items():
    if k in ['title', 'desc_start', 'desc_end'] and v == 0:
      print(filename)
      print(k)
      raise Exception

  return extract_dict


def extract_rst(extract_dict):
  """Extract relevant sections of rst file to a string buffer
  for docstring inputs.

  Args:
    extract_dict: dict.
      Dictionary of start and end positions of extracted sections from the
      rst file. Returned from parse_rst function.

  Returns:
    str. string buffer containing relevant rst info to form part of generated
    python file's docstring.
  """
  output = ''
  indent = '  '  # indent for generated python file
  TITLE_WRAP = 74  # Wrap title if too long (package specific)
  DESC_WRAP = 77  # Wrap description if too long (package specific)
  FORMAT_WRAP = 77  # Wrap format if too long (package specific)
  SOURCE_WRAP = 77  # Wrap source if too long (package specific)

  with open(extract_dict['file_name']) as f:
    for i, line in enumerate(f):
      line = line.rstrip(' ')
      if i == extract_dict['title']:
        if len(line) > TITLE_WRAP:
          output += line[:TITLE_WRAP] + '\n'
          next_line = line[TITLE_WRAP:]
          if not next_line.strip() == '':
            output += indent + next_line
        else:
          output += line
      if (i >= extract_dict['desc_start']) and \
              (i < extract_dict['desc_end']):
        if line == '\n':
          output += line
        else:
          if len(line) > DESC_WRAP:
            output += line[:DESC_WRAP] + '\n'
            next_line = line[DESC_WRAP:]
            if not next_line.strip() == '':
              output += indent + next_line
          else:
            output += indent + line
      if extract_dict['format_start'] > 0:
        if (i >= extract_dict['format_start']) and \
           (i < extract_dict['format_end']):
          if line == '\n':
            output += line
          else:
            if len(line) > FORMAT_WRAP:
              output += line[:FORMAT_WRAP] + '\n'
              next_line = line[FORMAT_WRAP:]
              if not next_line.strip() == '':
                output += indent + next_line
            else:
              output += indent + line
      if extract_dict['source_start'] > 0:
        if (i >= extract_dict['source_start']) and \
                (i < extract_dict['source_end']):
          if line == '\n':
            output += line
          else:
            if len(line) > SOURCE_WRAP:
              output += line[:SOURCE_WRAP] + '\n'
              next_line = line[SOURCE_WRAP:]
              if not next_line.strip() == '':
                output += indent + next_line
            else:
              output += indent + line
    output = output.replace('``', '`')  # replace double ``
  return output


def gen_context(row):
  """Generate context for jinja templated python file.

  Args:

    row: pandas row object.
      Single row of master csv file.

  Returns:

    Dictionary. The context dictionary required by jinja template to
    populate generated python file with docstring and source code.
  """
  URL_WRAP_LEN = 62  # Wrap long urls
  WRAP_INDENT = 10   # Indent required after wrap for PEP8 compliance
  function = row['function_name']  # function name in python file
  rst_loc = row['rst_files']  # read docstring for python file from rst file
  try:
    rows = int(row['rows'])
  except ValueError:
    print(function)
    rows = ''
  try:
    cols = int(row['cols'])
  except ValueError:
    print(function, rst_loc)
    cols = ''
  url = row['remote_base_url'] + row['remote_file_name']
  if len(url) > URL_WRAP_LEN:
    url = url[:URL_WRAP_LEN] + "' \\\n"
    url = url + " " * WRAP_INDENT + "'" + url[URL_WRAP_LEN:]
  save_filename = row['local_file_name']  # local file name
  try:
    desc = extract_rst(parse_rst(rst_loc))
  except:
    print('Exception occurred at : ', rst_loc)
    return None
  context = {'function': function,
             'desc': desc,
             'rows': rows,
             'cols': cols,
             'url': url,
             'file_name': save_filename,
             }
  return context


def render(tpl_path, context):
  """ Render jinja template to python file given context.

  Args:

    tpl_path: str.
      Path to the jinja template file (*.tpl).
    context: dict.
      Context dictionary to render template file to python source file.

  Returns:

    None.

  """
  path, filename = os.path.split(tpl_path)
  jinja_loader = jinja2.FileSystemLoader(path or './')
  jinja_env = jinja2.Environment(loader=jinja_loader)
  return jinja_env.get_template(filename).render(context)


def gen_data_test_files(row, source_file_template='./template.tpl',
                        source_file_path='./',
                        test_file_template='./test_template.tpl',
                        test_file_path='./'):
  """Generate python source files and python test files from templates

  Args:

    row: pandas row object.
      Single row of master csv file.
    source_file_template: str, optional.
      File name of template file to generate python source file.
    source_file_path: str, optional.
      Path to the location for generating python source file.
    test_file_template: str, optional.
      File name of template file to generate python test file.
    test_file_path: str, optional.
      Path to the location for generating python test file.

  Returns:

    None.

  """
  context = gen_context(row)
  if context is None:
    return
  file_str = render(source_file_template, context)
  test_file_str = render(test_file_template, context)
  with open(os.path.join(source_file_path, context['function'] + '.py'),
            'w') as f:
    f.write(file_str)
  with open(os.path.join(test_file_path,
                         'test_' + context['function'] + '.py'), 'w') as f:
    f.write(test_file_str)


def gen_init_file(dataset, init_file_template='./init_template.tpl',
                  init_path='./', import_prefix='observations.r'):
  """Generate python __init__.py file to expose modules from a template.

    Args:

      dataset: pandas dataframe.
        Pandas dataframe containing the entire master csv file.
      init_file_template: str, optional.
        File name of template file to generate __init__.py.
      init_path: str, optional.
        Path to the location for generating __init__.py.
      import_prefix: str, optional.
        Required import prefix in the __init__.py.

    Returns:

      None.
    """
  def import_names(x):
    return 'from ' + import_prefix + '.' + x + ' import ' + x

  def allowed_modules(x):
    return "    '" + x + "'"

  function_imports = '\n'.join(dataset.function_name.sort_values().
                               map(import_names))
  allowed_symbols = ',\n'.join(dataset.function_name.sort_values().
                               map(allowed_modules))
  init_file_str = render(init_file_template,
                         {'function_imports': function_imports,
                          'allowed_symbols': allowed_symbols})
  with open(os.path.join(init_path, '__init__.py'), 'w') as f:
    f.write(init_file_str)


def gen_observations_sources_from_csv(csv_master_file,
                                      source_file_template,
                                      source_file_path,
                                      test_file_template,
                                      test_file_path,
                                      init_file_template,
                                      init_file_path,
                                      import_prefix):
  """Generate observations ready python source, test, __init__.py files
  from a CSV master file.

  Args:

    csv_master_file: str.
      Master CSV file that contains relevant information to generate
      the source, test and __init__.py files. The format is very specific.
      Pls look at the dataset.csv file in the repo for format.
    source_file_template: str.
      File name of template file to generate python source file.
    source_file_path: str.
      Path to the location for generating python source file.
    test_file_template: str.
      File name of template file to generate python test file.
    test_file_path: str.
      Path to the location for generating python test file.
    init_file_template: str.
      File name of template file to generate __init__.py.
    init_path: str.
      Path to the location for generating __init__.py.
    import_prefix: str.
      Required import prefix in the __init__.py.

  Returns:

      None.
  """

  if not os.path.exists(source_file_path):
    os.makedirs(source_file_path)
  if not os.path.exists(test_file_path):
    os.makedirs(test_file_path)
  datasets = pd.read_csv(csv_master_file, encoding='ISO-8859-1')
  gen_init_file(datasets, init_file_template,
                init_file_path, import_prefix)
  for i in range(datasets.shape[0]):
    gen_data_test_files(datasets.iloc[i], source_file_template,
                        source_file_path, test_file_template,
                        test_file_path)


if __name__ == "__main__":
  import jinja2
  import pandas as pd

  parser = argparse.ArgumentParser()

  parser.add_argument('--csv_master',
                      type=str,
                      default='./datasets.csv',
                      help='Master CSV file required to generate observations '
                           'python files'
                      )

  parser.add_argument('--src_template',
                      type=str,
                      default='./templates/template.tpl',
                      help='Path to jinja template file for generating '
                           'python source files'
                      )

  parser.add_argument('--src_path',
                      type=str,
                      default='./observations/r/',
                      help='Path to generated python source files'
                      )

  parser.add_argument('--test_template',
                      type=str,
                      default='./templates/test_template.tpl',
                      help='Path to jinja template file for generating '
                           'python test files'
                      )

  parser.add_argument('--test_path',
                      type=str,
                      default='./tests/r',
                      help='Path to generated python test files'
                      )

  parser.add_argument('--init_template',
                      type=str,
                      default='./templates/init_template.tpl',
                      help='Path to jinja template file for generating '
                           '__init__.py file'
                      )

  parser.add_argument('--init_path',
                      type=str,
                      default='./observations/r/',
                      help='Path to generated __init__.py file'
                      )

  parser.add_argument('--import_prefix',
                      type=str,
                      default='observations.r',
                      help='import prefix in generated __init__.py file'
                      )

  results = parser.parse_args()
  gen_observations_sources_from_csv(csv_master_file=results.csv_master,
                                    source_file_template=results.src_template,
                                    source_file_path=results.src_path,
                                    test_file_template=results.test_template,
                                    test_file_path=results.test_path,
                                    init_file_template=results.init_template,
                                    init_file_path=results.init_path,
                                    import_prefix=results.import_prefix
                                    )
