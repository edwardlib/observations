# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bwght2(path):
  """bwght2

  Data loads lazily. Type data(bwght2) into the console.

  A data.frame with 1832 rows and 23 variables:

  -  mage. mother's age, years

  -  meduc. mother's educ, years

  -  monpre. month prenatal care began

  -  npvis. total number of prenatal visits

  -  fage. father's age, years

  -  feduc. father's educ, years

  -  bwght. birth weight, grams

  -  omaps. one minute apgar score

  -  fmaps. five minute apgar score

  -  cigs. avg cigarettes per day

  -  drink. avg drinks per week

  -  lbw. =1 if bwght <= 2000

  -  vlbw. =1 if bwght <= 1500

  -  male. =1 if baby male

  -  mwhte. =1 if mother white

  -  mblck. =1 if mother black

  -  moth. =1 if mother is other

  -  fwhte. =1 if father white

  -  fblck. =1 if father black

  -  foth. =1 if father is other

  -  lbwght. log(bwght)

  -  magesq. mage^2

  -  npvissq. npvis^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bwght2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1832 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bwght2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/bwght2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bwght2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
