# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fruitohms(path):
  """Electrical Resistance of Kiwi Fruit

  Data are from a study that examined how the electrical resistance of a
  slab of kiwifruit changed with the apparent juice content.

  This data frame contains the following columns:

  juice
      apparent juice content (percent)

  ohms
      electrical resistance (in ohms)

  Harker, F. R. and Maindonald J.H. 1994. Ripening of nectarine fruit.
  *Plant Physiology* 106: 165 - 171.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fruitohms.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 128 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fruitohms.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/fruitohms.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fruitohms.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
