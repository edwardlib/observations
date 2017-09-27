# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def twins_lungs(path):
  """TwinsLungs

  Comparing lung function for twins between rural and urban environments

  A dataset with 14 observations on the following 3 variables.

  `Pair`

  Code for the twin pair: `A` - `G`

  `Environ`

  Living environment: `Rural` or `Urban`

  `Percent`

  Percentage of radioactivity remaining in lungs

  “Urban factor and tracheobronchial clearance" by Per Camner and Klas
  Philipson in Archives of Environmental Health, V. 27 (1973), page 82.
  Data can be found in Introduction to Mathematical Statistics and its
  Applications, 2nd Edition by Richard J. Larson and Morris L. Marx.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `twins_lungs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'twins_lungs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/TwinsLungs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='twins_lungs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
