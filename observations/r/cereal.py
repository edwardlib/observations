# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cereal(path):
  """Cereal

  Breakfast cereals

  A dataset with 36 observations on the following 4 variables.

  `Cereal`

  Brandname of cereal

  `Calories`

  Calories per serving

  `Sugar`

  Grams of sugar per serving

  `Fiber`

  Grams of fiber per serving

  These data were collected by Patricia Benedict, Ronald Brahler, and
  Kenneth Motz, who read the nutritional labels on the boxes, in an
  attempt to learn whether cereals high in fiber are also high in sugar
  and calories. The cereals are all of those that were sold at Russo Stop

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cereal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cereal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Cereal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cereal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
