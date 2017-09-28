# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def train(path):
  """Stated Preferences for Train Traveling

  a cross-section from 1987

  *number of observations* : 2929

  *observation* : individuals

  *country* : Netherland

  A dataframe containing :

  id
      individual identifier

  choiceid
      choice identifier

  choice
      one of choice1, choice2

  pricez
      price of proposition z (z=1,2) in cents of guilders

  timez
      travel time of proposition z (z=1,2) in minutes

  comfortz
      comfort of proposition z (z=1,2), 0, 1 or 2 in decreasing comfort
      order

  changez
      number of changes for proposition z (z=1,2)

  Meijer, Erik and Jan Rouwendal (2005) “Measuring welfare effects in
  models with random coefficients”, *Journal of Applied Econometrics*,
  **forthcoming**.

  Ben–Akiva, M., D. Bolduc and M. Bradley (1993) “Estimation of travel
  choice models with randomly distributed values of time”, *Transportation
  Research Record*, **1413**, 88–97.

  Carson, R.T., L. Wilks and D. Imber (1994) “Valuing the preservation of
  Australia's Kakadu conservation zone”, *Oxford Economic Papers*, **46**,
  727–749.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `train.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2929 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'train.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Train.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='train.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
