# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def heptathlon(path):
  """Olympic Heptathlon Seoul 1988

  Results of the olympic heptathlon competition, Seoul, 1988.

  A data frame with 25 observations on the following 8 variables.

  `hurdles`
      results 100m hurdles.

  `highjump`
      results high jump.

  `shot`
      results shot.

  `run200m`
      results 200m race.

  `longjump`
      results long jump.

  `javelin`
      results javelin.

  `run800m`
      results 800m race.

  `score`
      total score.

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `heptathlon.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'heptathlon.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/heptathlon.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='heptathlon.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
