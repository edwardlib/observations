# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sparrows(path):
  """Sparrows

  Weight and wing length for a sample of Savannah sparrows

  A dataset with 116 observations on the following 3 variables.

  `Treatment`

  Nest adjustment: `control`, `enlarged`, or `reduced`

  `Weight`

  Weight (in grams)

  `WingLength`

  Wing length (in mm)

  We thank Priscilla Erickson and Professor Robert Mauck from the
  Department of Biology at Kenyon College for allowing us to use these

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sparrows.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 116 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sparrows.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Sparrows.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sparrows.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
