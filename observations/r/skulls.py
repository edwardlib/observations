# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def skulls(path):
  """Egyptian Skulls

  Measurements made on Egyptian skulls from five epochs.

  A data frame with 150 observations on the following 5 variables.

  `epoch`
      the epoch the skull as assigned to, a factor with levels `c4000BC`
      `c3300BC`, `c1850BC`, `c200BC`, and `cAD150`, where the
      years are only given approximately, of course.

  `mb`
      maximum breaths of the skull.

  `bh`
      basibregmatic heights of the skull.

  `bl`
      basialiveolar length of the skull.

  `nh`
      nasal heights of the skull.

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `skulls.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 150 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'skulls.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/skulls.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='skulls.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
