# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pig_feed(path):
  """PigFeed

  Effects of additives to pig feed on weight gain

  A dataset with 12 observations on the following 3 variables.

  `WgtGain`

  Daily wight gain (hundredths of a pound over 1.00)

  `Antibiotic`

  Antibiotic in the feed? `No` or `Yes`

  `B12`

  Vitamin B12 in the feed? `No` or `Yes`

  Data are found in Statistical Methods by George W. Snedecor and William
  G. Cochran (1967). Ames, IA: The Iowa State University Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pig_feed.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pig_feed.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/PigFeed.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pig_feed.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
