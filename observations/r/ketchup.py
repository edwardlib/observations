from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ketchup(path):
  """Choice of Brand for Ketchup

  a cross-section

  *number of observations* : 4956

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  hid
      individuals identifiers

  id
      purchase identifiers

  choice
      one of heinz, hunts, delmonte, stb (store brand)

  price.z
      price of brand z

  Kim, Byong–Do, Robert C. Blattberg and Peter E. Rossi (1995) “Modeling
  the distribution of price sensitivity and implications for optimal
  retail pricing”, *Journal of Business Economics and Statistics*,
  **13(3)**, 291.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ketchup.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4956 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ketchup.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/Ecdat/Ketchup.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ketchup.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
