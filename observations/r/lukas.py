from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lukas(path):
  """An example pedigree

  A multi-generational pedigree containing individual, father, mother IDs
  and sex.

  An example pedigree


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lukas.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 85 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lukas.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/gap/lukas.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lukas.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
