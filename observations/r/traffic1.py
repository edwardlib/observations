# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def traffic1(path):
  """traffic1

  Data loads lazily. Type data(traffic1) into the console.

  A data.frame with 51 rows and 13 variables:

  -  state.

  -  admn90. =1 if admin. revoc., '90

  -  admn85. =1 if admin. revoc., '85

  -  open90. =1 if open cont. law, '90

  -  open85. =1 if open cont. law, '85

  -  dthrte90. deaths per 100 mill. miles, '90

  -  dthrte85. deaths per 100 mill. miles, '85

  -  speed90. =1 if 65 mph, 1990

  -  speed85. =0 always

  -  cdthrte. dthrte90 - dthrte85

  -  cadmn. admn90 - admn85

  -  copen. open90 - open85

  -  cspeed. speed90 - speed85

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `traffic1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'traffic1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/traffic1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='traffic1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
