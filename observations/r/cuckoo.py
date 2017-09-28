# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cuckoo(path):
  """Cuckoo

  Lengths of cuckoo eggs laid in other birds' nests

  A dataset with 120 observations on the following 2 variables.

  `Bird`

  Type of bird nest: `mdw_pipit` (meadow pipit), `tree_pipit`,

  `hedge_sparrow`, `robin`, `wagtail`, or `wren`

  `Length`

  Cuckoo egg length (in mm)

  Downloaded from DASL at
  http://lib.stat.cmu.edu/DASL/Datafiles/cuckoodat.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cuckoo.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 120 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cuckoo.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Cuckoo.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cuckoo.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
