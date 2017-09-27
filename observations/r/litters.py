# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def litters(path):
  """Mouse Litters

  Data on the body and brain weights of 20 mice, together with the size of
  the litter. Two mice were taken from each litter size.

  This data frame contains the following columns:

  lsize
      litter size

  bodywt
      body weight

  brainwt
      brain weight

  Wainright P, Pelkman C and Wahlsten D 1989. The quantitative
  relationship between nutritional effects on preweaning growth and
  behavioral development in mice. Developmental Psychobiology 22: 183-193.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `litters.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'litters.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/litters.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='litters.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
