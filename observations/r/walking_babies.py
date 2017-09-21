# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def walking_babies(path):
  """WalkingBabies

  An experiment to see if special exercises help babies learn to walk
  sooner

  A dataset with 24 observations on the following 2 variables.

  `Group`

  Treatments: `exercise control`, `final report`,
  `special exercises`, or `weekly report`

  `Age`

  Age (in months) when first walking

  Zelazo, Phillip R., Nancy Ann Zelazo, and Sarah Kolb (1972), “Walking in

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `walking_babies.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'walking_babies.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/Stat2Data/WalkingBabies.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='walking_babies.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
