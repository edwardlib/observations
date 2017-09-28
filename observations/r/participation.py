# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def participation(path):
  """Labor Force Participation

  a cross-section

  *number of observations* : 872

  *observation* : individuals

  *country* : Switzerland

  A dataframe containing :

  lfp
      labour force participation ?

  lnnlinc
      the log of nonlabour income

  age
      age in years divided by 10

  educ
      years of formal education

  nyc
      the number of young children (younger than 7)

  noc
      number of older children

  foreign
      foreigner ?

  Gerfin, Michael (1996) “Parametric and semiparametric estimation of the
  binary response”, *Journal of Applied Econometrics*, **11(3)**, 321-340.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `participation.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 872 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'participation.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Participation.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='participation.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
