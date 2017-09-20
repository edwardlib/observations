from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ruspini(path):
  """Ruspini Data

  The Ruspini data set, consisting of 75 points in four groups that is
  popular for illustrating clustering techniques.

  A data frame with 75 observations on 2 variables giving the x and y
  coordinates of the points, respectively.

  E. H. Ruspini (1970) Numerical methods for fuzzy clustering. *Inform.
  Sci.* **2**, 319–350.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ruspini.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 75 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ruspini.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/cluster/ruspini.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ruspini.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
