# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def roller(path):
  """Lawn Roller Data

  The `roller` data frame has 10 rows and 2 columns. Different weights
  of roller were rolled over different parts of a lawn, and the depression
  was recorded.

  This data frame contains the following columns:

  weight
      a numeric vector consisting of the roller weights

  depression
      the depth of the depression made in the grass under the roller

  Stewart, K.M., Van Toor, R.F., Crosbie, S.F. 1988. Control of grass grub
  (Coleoptera: Scarabaeidae) with rollers of different design. N.Z.
  Journal of Experimental Agriculture 16: 141-150.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `roller.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'roller.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/roller.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='roller.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
