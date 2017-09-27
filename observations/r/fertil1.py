# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fertil1(path):
  """fertil1

  Data loads lazily. Type data(fertil1) into the console.

  A data.frame with 1129 rows and 27 variables:

  -  year. 72 to 84, even

  -  educ. years of schooling

  -  meduc. mother's education

  -  feduc. father's education

  -  age. in years

  -  kids. # children ever born

  -  black. = 1 if black

  -  east. = 1 if lived in east at 16

  -  northcen. = 1 if lived in nc at 16

  -  west. = 1 if lived in west at 16

  -  farm. = 1 if on farm at 16

  -  othrural. = 1 if other rural at 16

  -  town. = 1 if lived in town at 16

  -  smcity. = 1 if in small city at 16

  -  y74. = 1 if year = 74

  -  y76.

  -  y78.

  -  y80.

  -  y82.

  -  y84.

  -  agesq. age^2

  -  y74educ.

  -  y76educ.

  -  y78educ.

  -  y80educ.

  -  y82educ.

  -  y84educ.

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fertil1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1129 rows and 27 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fertil1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/fertil1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fertil1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
