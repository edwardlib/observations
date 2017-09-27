# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cracker(path):
  """Choice of Brand for Crakers

  a cross-section

  *number of observations* : 3292

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  id
      individuals identifiers

  choice
      one of sunshine, kleebler, nabisco, private

  disp.z
      is there a display for brand z ?

  feat.z
      is there a newspaper feature advertisement for brand z ?

  price.z
      price of brand z

  Jain, Dipak C., Naufel J. Vilcassim and Pradeep K. Chintagunta (1994) “A
  random–coefficients logit brand–choice model applied to panel data”,
  *Journal of Business and Economics Statistics*, **12(3)**, 317.

  Paap, R. and Philip Hans Frances (2000) “A dynamic multinomial probit
  model for brand choices with different short–run effects of marketing
  mix variables”, *Journal of Applied Econometrics*, **15(6)**, 717–744.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cracker.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3292 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cracker.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Cracker.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cracker.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
