# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wght_loss_incentive4(path):
  """WeightLossIncentive4

  Weight loss after four months with/without a financial incentive

  A dataset with 36 observations on the following 2 variables.

  `WeightLoss`

  weight loss (in pounds) after 4 months

  `Group`

  Treatment group: `Control` or `Incentive`

  “Financial incentive-based approaches for weight loss," Journal of the
  American Medical Association by Volpp, John, Troxel, et. al., Vol. 200,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wght_loss_incentive4.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wght_loss_incentive4.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/Stat2Data/WeightLossIncentive4.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wght_loss_incentive4.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
