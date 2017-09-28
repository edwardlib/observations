# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def calcium(path):
  """Calcium Uptake Data

  The `calcium` data frame has 27 rows and 2 columns.

  Howard Grimes from the Botany Department, North Carolina State
  University, conducted an experiment for biochemical analysis of
  intracellular storage and transport of calcium across plasma membrane.
  Cells were suspended in a solution of radioactive calcium for a certain
  length of time and then the amount of radioactive calcium that was
  absorbed by the cells was measured. The experiment was repeated
  independently with 9 different times of suspension each replicated 3
  times.

  This data frame contains the following columns:

  `time`
      The time (in minutes) that the cells were suspended in the solution.

  `cal`
      The amount of calcium uptake (nmoles/mg).

  The data were obtained from

  Rawlings, J.O. (1988) *Applied Regression Analysis*. Wadsworth and
  Brooks/Cole Statistics/Probability Series.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `calcium.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'calcium.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/calcium.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='calcium.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
