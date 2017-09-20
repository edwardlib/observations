from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def expendshares(path):
  """expendshares

  Data loads lazily. Type data(expendshares) into the console.

  A data.frame with 1519 rows and 13 variables:

  -  sfood. share of food expenditures (out of total)

  -  sfuel. share of fuel expenditures

  -  sclothes. share of clothing expenditures

  -  salcohol. share of alcohol expenditures

  -  stransport. share of transportation expenditures

  -  sother. share of other expenditures

  -  totexpend. total expenditure, British pounds per week

  -  income. family income, British pounds per week

  -  age. age of household head

  -  kids. number of children: 1 or 2

  -  ltotexpend. log(totexpend)

  -  lincome. log(income)

  -  agesq. age^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `expendshares.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1519 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'expendshares.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/wooldridge/expendshares.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='expendshares.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
