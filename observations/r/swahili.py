from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def swahili(path):
  """Swahili

  Attitudes towards the Swahili language among Kenyan school children

  A dataset with 480 observations on the following 4 variables.

  `Province`

  `NAIROBI` or `PWANI`

  `Sex`

  `female` or `male`

  `Attitude.Score`

  Score (out a possible 200 points) on a survey of attitude towards the
  Swahili language

  `School`

  Code for the school: `A` through `L`


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `swahili.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 480 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'swahili.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/Stat2Data/Swahili.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='swahili.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
