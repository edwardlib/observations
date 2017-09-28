# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grav(path):
  """Acceleration Due to Gravity

  The `gravity` data frame has 81 rows and 2 columns.

  The `grav` data set has 26 rows and 2 columns.

  Between May 1934 and July 1935, the National Bureau of Standards in
  Washington D.C. conducted a series of experiments to estimate the
  acceleration due to gravity, *g*, at Washington. Each experiment
  produced a number of replicate estimates of *g* using the same
  methodology. Although the basic method remained the same for all
  experiments, that of the reversible pendulum, there were changes in
  configuration.

  The `gravity` data frame contains the data from all eight experiments.
  The `grav` data frame contains the data from the experiments 7 and 8.
  The data are expressed as deviations from 980.000 in centimetres per
  second squared.

  This data frame contains the following columns:

  `g`
      The deviation of the estimate from 980.000 centimetres per second
      squared.

  `series`
      A factor describing from which experiment the estimate was derived.

  The data were obtained from

  Cressie, N. (1982) Playing safe with misweighted means. *Journal of the
  American Statistical Association*, **77**, 754–759.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grav.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grav.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/grav.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grav.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
