# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def retinopathy(path):
  """Diabetic Retinopathy

  A trial of laser coagulation as a treatment to delay diabetic
  retinopathy.

  A data frame with 394 observations on the following 9 variables.

  `id`
      numeric subject id

  `laser`
      type of laser used: `xenon` `argon`

  `eye`
      which eye was treated: `right` `left`

  `age`
      age at diagnosis of diabetes

  `type`
      type of diabetes: `juvenile` `adult`, (diagnosis before age 20)

  `trt`
      0 = control eye, 1 = treated eye

  `futime`
      time to loss of vision or last follow-up

  `status`
      0 = censored, 1 = loss of vision in this eye

  `risk`
      a risk score for the eye. This high risk subset is defined as a
      score of 6 or greater in at least one eye.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `retinopathy.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 394 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'retinopathy.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/retinopathy.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='retinopathy.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
