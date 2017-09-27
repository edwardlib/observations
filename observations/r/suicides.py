# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def suicides(path):
  """Crowd Baiting Behaviour and Suicides

  Data from a study carried out to investigate the causes of jeering or
  baiting behaviour by a crowd when a person is threatening to commit
  suicide by jumping from a high building.

  A two-way classification, see `table`.

  L. Mann (1981), The baiting crowd in episodes of threatened suicide.
  *Journal of Personality and Social Psychology*, **41**, 703–709.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `suicides.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'suicides.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/suicides.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='suicides.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
