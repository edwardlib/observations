from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def geophones(path):
  """Seismic Timing Data

  The `geophones` data frame has 56 rows and 2 columns. Thickness of a
  layer of Alberta substratum as measured by a line of geophones.

  This data frame contains the following columns:

  distance
      location of geophone.

  thickness
      time for signal to pass through substratum.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `geophones.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'geophones.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/DAAG/geophones.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='geophones.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
