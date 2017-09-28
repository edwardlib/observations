# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def stormer(path):
  """The Stormer Viscometer Data

  The stormer viscometer measures the viscosity of a fluid by measuring
  the time taken for an inner cylinder in the mechanism to perform a fixed
  number of revolutions in response to an actuating weight. The viscometer
  is calibrated by measuring the time taken with varying weights while the
  mechanism is suspended in fluids of accurately known viscosity. The data
  comes from such a calibration, and theoretical considerations suggest a
  nonlinear relationship between time, weight and viscosity, of the form
  `Time = (B1*Viscosity)/(Weight - B2) + E` where `B1` and `B2` are
  unknown parameters to be estimated, and `E` is error.

  The data frame contains the following components:

  `Viscosity`
      viscosity of fluid.

  `Wt`
      actuating weight.

  `Time`
      time taken.

  E. J. Williams (1959) *Regression Analysis.* Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `stormer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'stormer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/stormer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='stormer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
