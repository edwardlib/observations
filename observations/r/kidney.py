# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kidney(path):
  """Kidney catheter data

  Data on the recurrence times to infection, at the point of insertion of
  the catheter, for kidney patients using portable dialysis equipment.
  Catheters may be removed for reasons other than infection, in which case
  the observation is censored. Each patient has exactly 2 observations.

  This data has often been used to illustrate the use of random effects
  (frailty) in a survival model. However, one of the males (id 21) is a
  large outlier, with much longer survival than his peers. If this
  observation is removed no evidence remains for a random subject effect.

  patient:

  id

  time:

  time

  status:

  event status

  age:

  in years

  sex:

  1=male, 2=female

  disease:

  disease type (0=GN, 1=AN, 2=PKD, 3=Other)

  frail:

  frailty estimate from original paper

  CA McGilchrist, CW Aisbett (1991), Regression with frailty in survival
  analysis. *Biometrics* **47**, 461–66.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kidney.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 76 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kidney.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/kidney.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kidney.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
