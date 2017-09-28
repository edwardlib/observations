# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def respiratory(path):
  """Respiratory Illness Data

  The respiratory status of patients recruited for a randomised clinical
  multicenter trial.

  A data frame with 555 observations on the following 7 variables.

  `centre`
      the study center, a factor with levels `1` and `2`.

  `treatment`
      the treatment arm, a factor with levels `placebo` and
      `treatment`.

  `sex`
      a factor with levels `female` and `male`.

  `age`
      the age of the patient.

  `status`
      the respiratory status (response variable), a factor with levels
      `poor` and `good`.

  `month`
      the month, each patient was examined at months `0`, `1`, `2`,
      `3` and `4`.

  `subject`
      the patient ID, a factor with levels `1` to `111`.

  C. S. Davis (1991), Semi-parametric and non-parametric methods for the
  analysis of repeated measurements with applications to clinical trials.
  *Statistics in Medicine*, **10**, 1959–1980.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `respiratory.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 444 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'respiratory.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/respiratory.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='respiratory.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
