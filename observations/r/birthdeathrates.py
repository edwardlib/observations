from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def birthdeathrates(path):
  """Birth and Death Rates Data

  Birth and death rates for 69 countries.

  A data frame with 69 observations on the following 2 variables.

  `birth`
      birth rate.

  `death`
      death rate.

  J. A. Hartigan (1975), *Clustering Algorithms*. John Wiley & Sons, New
  York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `birthdeathrates.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 69 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'birthdeathrates.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/HSAUR/birthdeathrates.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='birthdeathrates.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
