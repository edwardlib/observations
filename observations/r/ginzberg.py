# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ginzberg(path):
  """Data on Depression

  The `Ginzberg` data frame has 82 rows and 6 columns. The data are for
  psychiatric patients hospitalized for depression.

  This data frame contains the following columns:

  simplicity
      Measures subject's need to see the world in black and white.

  fatalism
      Fatalism scale.

  depression
      Beck self-report depression scale.

  adjsimp
      Adjusted Simplicity: Simplicity adjusted (by regression) for other
      variables thought to influence depression.

  adjfatal
      Adjusted Fatalism.

  adjdep
      Adjusted Depression.

  Personal communication from Georges Monette, Department of Mathematics
  and Statistics, York University, with the permission of the original
  investigator.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ginzberg.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 82 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ginzberg.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Ginzberg.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ginzberg.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
