from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def admnrev(path):
  """admnrev

  Data loads lazily. Type data(admnrev) into the console.

  A data.frame with 153 rows and 5 variables:

  -  state. state postal code

  -  year. 85, 90, or 95

  -  admnrev. =1 if admin. revoc. law

  -  daysfrst. days suspended, first offense

  -  daysscnd. days suspended, second offense

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `admnrev.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 153 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'admnrev.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/wooldridge/admnrev.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='admnrev.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
