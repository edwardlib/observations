# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mathlevel(path):
  """Level of Calculus Attained for Students Taking Advanced Micro–economics

  a cross-section from 1983 to 1986

  *number of observations* : 609

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  mathlevel
      highest level of math attained , an ordered factor with levels 170,
      171a, 172, 171b, 172b, 221a, 221b

  sat
      sat Math score

  language
      foreign language proficiency ?

  sex
      male, female

  major
      one of other, eco, oss (other social sciences), ns (natural
      sciences), hum (humanities)

  mathcourse
      number of courses in advanced math (0 to 3)

  physiccourse
      number of courses in physics (0 to 2)

  chemistcourse
      number of courses in chemistry (0 to 2)

  Butler, J.S., T. Aldrich Finegan and John J. Siegfried (1998) “Does more
  calculus improve student learning in intermediate micro and
  macroeconomic theory ?”, *Journal of Applied Econometrics*, **13(2)**,
  april, 185–202.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mathlevel.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 609 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mathlevel.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Mathlevel.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mathlevel.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
