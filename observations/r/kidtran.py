from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kidtran(path):
  """data from Section 1.7

  The `kidtran` data frame has 863 rows and 6 columns.

  This data frame contains the following columns:

  obs
      Observation number

  time
      Time to death or on-study time

  delta
      Death indicator (0=alive, 1=dead)

  gender
      1=male, 2=female

  race
      1=white, 2=black

  age
      Age in years

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kidtran.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 863 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kidtran.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/KMsurv/kidtran.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kidtran.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
