# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mignonette(path):
  """Darwin's Wild Mignonette Data

  Data which compare the heights of crossed plants with self-fertilized
  plants. Plants were paired within the pots in which they were grown,
  with one on one side and one on the other.

  This data frame contains the following columns:

  cross
      heights of the crossed plants

  self
      heights of the self-fertilized plants

  Darwin, Charles. 1877. The Effects of Cross and Self Fertilisation in
  the Vegetable Kingdom. Appleton and Company, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mignonette.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mignonette.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/mignonette.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mignonette.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
