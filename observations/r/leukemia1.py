# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leukemia1(path):
  """Leukemia

  Treatment results for leukemia patients

  A dataset with 51 observations on the following 9 variables.

  `Age`

  Age at diagnosis (in years)

  `Smear`

  Differential percentage of blasts

  `Infil`

  Percentage of absolute marrow leukemia infiltrate

  `Index`

  Percentage labeling index of the bone marrow leukemia cells

  `Blasts`

  Absolute number of blasts, in thousands

  `Temp`

  Highest temperature of the patient prior to treatment, in degrees
  Farenheit

  `Resp`

  `1`\ =responded to treatment or `0`\ =failed to respond

  `Time`

  Survival time from diagnosis (in months)

  `Status`

  `0`\ =dead or `1`\ =alive

  Data come from Statistical Analysis Using S-Plus (Brian S. Everitt;

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leukemia1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leukemia1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Leukemia.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leukemia1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
