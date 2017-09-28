# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wtloss(path):
  """Weight Loss Data from an Obese Patient

  The data frame gives the weight, in kilograms, of an obese patient at 52
  time points over an 8 month period of a weight rehabilitation programme.

  This data frame contains the following columns:

  `Days`
      time in days since the start of the programme.

  `Weight`
      weight in kilograms of the patient.

  Dr T. Davies, Adelaide.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wtloss.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 52 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wtloss.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/wtloss.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wtloss.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
