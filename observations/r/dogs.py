# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dogs(path):
  """Cardiac Data for Domestic Dogs

  The `dogs` data frame has 7 rows and 2 columns.

  Data on the cardiac oxygen consumption and left ventricular pressure
  were gathered on 7 domestic dogs.

  This data frame contains the following columns:

  mvo
      Cardiac Oxygen Consumption

  lvp
      Left Ventricular Pressure

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dogs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dogs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/dogs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dogs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
