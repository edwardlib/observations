# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cement(path):
  """Heat Evolved by Setting Cements

  Experiment on the heat evolved in the setting of each of 13 cements.

  `x1, x2, x3, x4`
      Proportions (%) of active ingredients.

  `y`
      heat evolved in cals/gm.

  Woods, H., Steinour, H.H. and Starke, H.R. (1932) Effect of composition
  of Portland cement on heat evolved during hardening. *Industrial
  Engineering and Chemistry*, **24**, 1207–1214.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cement.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 312 rows and 30 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cement.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/cement.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cement.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
