# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def thurstone_33(path):
  """Seven data sets showing a bifactor solution.

  Holzinger-Swineford (1937) introduced the bifactor model of a general
  factor and uncorrelated group factors. The Holzinger data sets are
  original 14 \* 14 matrix from their paper as well as a 9 \*9 matrix used
  as an example by Joreskog. The Thurstone correlation matrix is a 9 \* 9
  matrix of correlations of ability items. The Reise data set is 16 \* 16
  correlation matrix of mental health items. The Bechtholdt data sets are
  both 17 x 17 correlation matrices of ability tests.

  | Holzinger: Holzinger and Swineford (1937)
  | Reise: Steve Reise (personal communication)
  | sem help page (for Thurstone)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `thurstone_33.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'thurstone_33.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Thurstone.33.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='thurstone_33.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
