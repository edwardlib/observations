# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hirose(path):
  """Failure Time of PET Film

  The `hirose` data frame has 44 rows and 3 columns.

  PET film is used in electrical insulation. In this accelerated life test
  the failure times for 44 samples in gas insulated transformers. 4
  different voltage levels were used.

  This data frame contains the following columns:

  `volt`
      The voltage (in kV).

  `time`
      The failure or censoring time in hours.

  `cens`
      The censoring indicator; `1` means right-censored data.

  The data were obtained from

  Hirose, H. (1993) Estimation of threshold stress in accelerated
  life-testing. *IEEE Transactions on Reliability*, **42**, 650–657.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hirose.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 44 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hirose.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/hirose.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hirose.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
