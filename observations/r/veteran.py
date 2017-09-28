# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def veteran(path):
  """Veterans' Administration Lung Cancer study

  Randomised trial of two treatment regimens for lung cancer. This is a
  standard survival analysis data set.

  trt:

  1=standard 2=test

  celltype:

  1=squamous, 2=smallcell, 3=adeno, 4=large

  time:

  survival time

  status:

  censoring status

  karno:

  Karnofsky performance score (100=good)

  diagtime:

  months from diagnosis to randomisation

  age:

  in years

  prior:

  prior therapy 0=no, 1=yes

  D Kalbfleisch and RL Prentice (1980), *The Statistical Analysis of

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `veteran.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 137 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'veteran.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/veteran.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='veteran.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
