# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wght_loss_incentive7(path):
  """WeightLossIncentive7

  Weight loss after seven months with/without a financial incentive

  A dataset with 33 observations on the following 2 variables.

  `Group`

  Treatment group: `Control` or `Incentive`

  `Month7Loss`

  Weight loss (in pounds) after seven months

  “Financial incentive-based approaches for weight loss," Journal of the
  American Medical Association by Volpp, John, Troxel, et. al., Vol. 200,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wght_loss_incentive7.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 33 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wght_loss_incentive7.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/WeightLossIncentive7.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wght_loss_incentive7.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
