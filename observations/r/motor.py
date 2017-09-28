# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def motor(path):
  """Data from a Simulated Motorcycle Accident

  The `motor` data frame has 94 rows and 4 columns. The rows are
  obtained by removing replicate values of `time` from the dataset
  `mcycle`. Two extra columns are added to allow for strata with a
  different residual variance in each stratum.

  This data frame contains the following columns:

  `times`
      The time in milliseconds since impact.

  `accel`
      The recorded head acceleration (in g).

  `strata`
      A numeric column indicating to which of the three strata (numbered
      1, 2 and 3) the observations belong.

  `v`
      An estimate of the residual variance for the observation. `v` is
      constant within the strata but a different estimate is used for each
      of the three strata.

  The data were obtained from

  Silverman, B.W. (1985) Some aspects of the spline smoothing approach to
  non-parametric curve fitting. *Journal of the Royal Statistical Society,
  B*, **47**, 1–52.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `motor.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 94 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'motor.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/motor.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='motor.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
