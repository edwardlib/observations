# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def azdrg112(path):
  """azdrg112

  The data set relates to the hospital length of stay for patients having
  a CABG or PTCA (typel) heart procedure. The data comes from the 1995
  Arizona Medicare data for DRG (Diagnostic Related Group) 112. Other
  predictors include gender(1=female) and age75 (1-age 75+). Type is
  labeled as 1=emergency or urgent admission; 0= elective. Length of stay
  (los) ranges from 1 to 53 days.

  A data frame with 1,798 observations on the following 4 variables.

  `los`
      hospital length of stay: 1-53 days

  `gender`
      1=male; 0=female

  `type1`
      1=emergency/urgent admission; 0=elective admission

  `age75`
      1=age>75; 0=age<=75

  DRG 112 data from the 1995 Arizona Medicare (MedPar) State files

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `azdrg112.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1798 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'azdrg112.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/azdrg112.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='azdrg112.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
