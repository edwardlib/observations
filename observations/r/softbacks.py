from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def softbacks(path):
  """Measurements on a Selection of Paperback Books

  This is a subset of the `allbacks` data frame which gives measurements
  on the volume and weight of 8 paperback books.

  This data frame contains the following columns:

  volume
      a numeric vector giving the book volumes in cubic centimeters

  weight
      a numeric vector giving the weights in grams

  The bookshelf of J. H. Maindonald.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `softbacks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'softbacks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/DAAG/softbacks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='softbacks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
