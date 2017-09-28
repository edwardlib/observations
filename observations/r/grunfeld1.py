# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grunfeld1(path):
  """Grunfeld's Investment Data

  A balanced panel of 10 observational units (firms) from 1935 to 1954

  *total number of observations* : 200

  *observation* : production units

  *country* : United States

  A data frame containing :

  firm
      observation

  year
      date

  inv
      gross Investment

  value
      value of the firm

  capital
      stock of plant and equipment

  Online complements to Baltagi (2001):

  http://www.wiley.com/legacy/wileychi/baltagi/
  http://www.wiley.com/legacy/wileychi/baltagi/supp/Grunfeld.fil

  Online complements to Baltagi (2013):

http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=4338&itemId=111867232
  1&resourceId=13452

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grunfeld1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 200 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grunfeld1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/Grunfeld.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grunfeld1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
