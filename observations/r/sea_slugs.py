# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sea_slugs(path):
  """Sea Slugs

  Metamorphose rates for sea slugs exposed to different water samples

  A dataset with 36 observations on the following 2 variables.

  `Time`

  Minutes after tide come in

  `Percent`

  Proportion of 15 sea slug larvae that metamorphose

  Data downloaded from
  http://www.stat.ucla.edu/projects/datasets/seaslug-explanation.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sea_slugs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sea_slugs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/SeaSlugs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sea_slugs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
