# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lactic(path):
  """Lactic Acid Concentration Measurement Data

  Data on the Calibration of an Instrument that Measures Lactic Acid
  Concentration in Blood, from Afifi and Azen (1979) - comparing the true
  concentration X with the measured value Y.

  A data frame with 20 observations on the following 2 variables.

  `X`
      True Concentration

  `Y`
      Instrument

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.62, table 10.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lactic.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lactic.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/lactic.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lactic.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
