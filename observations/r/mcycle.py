# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mcycle(path):
  """Data from a Simulated Motorcycle Accident

  A data frame giving a series of measurements of head acceleration in a
  simulated motorcycle accident, used to test crash helmets.

  `times`
      in milliseconds after impact.

  `accel`
      in g.

  Silverman, B. W. (1985) Some aspects of the spline smoothing approach to
  non-parametric curve fitting. *Journal of the Royal Statistical Society
  series B* **47**, 1–52.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mcycle.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 133 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mcycle.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/mcycle.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mcycle.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
