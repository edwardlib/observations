# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def slp75_81(path):
  """slp75\_81

  Data loads lazily. Type data(slp75\_81) into the console.

  A data.frame with 239 rows and 20 variables:

  -  age75. age in 1975

  -  educ75. years educ in '75

  -  educ81. years educ in '81

  -  gdhlth75. = 1 if good hlth in '75

  -  gdhlth81. =1 if good hlth in '81

  -  male. =1 if male

  -  marr75. = 1 if married in '75

  -  marr81. =1 if married in '81

  -  slpnap75. mins slp wk, inc naps, '75

  -  slpnap81. mins slp wk, inc naps, '81

  -  totwrk75. minutes worked per week, '75

  -  totwrk81. minutes worked per week, '81

  -  yngkid75. = 1 if child < 3, '75

  -  yngkid81. =1 if child < 3, '81

  -  ceduc. change in educ

  -  cgdhlth. change in gdhlth

  -  cmarr. change in marr

  -  cslpnap. change in slpnap

  -  ctotwrk. change in totwrk

  -  cyngkid. change in yngkid

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `slp75_81.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 239 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'slp75_81.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/slp75_81.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='slp75_81.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
