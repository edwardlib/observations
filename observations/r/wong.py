# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wong(path):
  """Post-Coma Recovery of IQ

  The `Wong` data frame has 331 row and 7 columns. The observations are
  longitudinal data on recovery of IQ after comas of varying duration for
  200 subjects.

  This data frame contains the following columns:

  `id`
      patient ID number.

  `days`
      number of days post coma at which IQs were measured.

  `duration`
      duration of the coma in days.

  `sex`
      a factor with levels `Female` and `Male`.

  `age`
      in years at the time of injury.

  `piq`
      performance (i.e., mathematical) IQ.

  `viq`
      verbal IQ.

  Wong, P. P., Monette, G., and Weiner, N. I. (2001) Mathematical models
  of cognitive recovery. *Brain Injury*, **15**, 519–530.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wong.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 331 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wong.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Wong.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wong.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
