# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fertility(path):
  """Fertility

  Fertility measurements for a sample of women

  A dataset with 333 observations on the following 10 variables.

  `Age`

  Age (in years)

  `LowAFC`

  Smallest antral follicle count

  `MeanAFC`

  Average antral follicle count

  `FSH`

  Maximum follicle stimulating hormone level

  `E2`

  Fertility level

  `MaxE2`

  Maximum fertility level

  `MaxDailyGn`

  Maximum daily gonadotropin level

  `TotalGn`

  Total gonadotropin level

  `Oocytes`

  Number of egg cells

  `Embryos`

  Number of embryos

  We thank Dr. Priya Maseelall and her research team for sharing these

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fertility.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 333 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fertility.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Fertility.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fertility.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
