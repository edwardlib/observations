# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mental_health(path):
  """Mental Health Admissions

  Admissions to a mental health emergency room and full moons

  A dataset with 36 observations on the following 3 variables.

  `Month`

  Month of the year

  `Moon`

  Relatinship to full moon: `After`, `Before`, or `During`

  `Admission`

  Number of emergency room admissions

  Introduction to Mathematical Statistics and its Applications by Richard
  J. Larsen and Morris L. Marx. Prentice Hall:Englewood Cliffs, NJ, 1986.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mental_health.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mental_health.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MentalHealth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mental_health.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
