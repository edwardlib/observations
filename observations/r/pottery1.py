# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pottery1(path):
  """Romano-British Pottery Data

  Chemical composition of Romano-British pottery.

  A data frame with 45 observations on the following 9 chemicals.

  Al2O3
      aluminium trioxide.

  Fe2O3
      iron trioxide.

  MgO
      magnesium oxide.

  CaO
      calcium oxide.

  Na2O
      natrium oxide.

  K2O
      calium oxide.

  TiO2
      titanium oxide.

  MnO
      mangan oxide.

  BaO
      barium oxide.

  A. Tubb and N. J. Parker and G. Nickless (1980), The analysis of
  Romano-British pottery by atomic absorption spectrophotometry.
  *Archaeometry*, **22**, 153–171.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pottery1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pottery1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/pottery.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pottery1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
