# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nswpsid1(path):
  """Labour Training Evaluation Data

  This data frame contains 2787 rows and 10 columns. These data are
  pertinent to an investigation of the way that earnings changed, between
  1974-1975 and 1978, in the absence of training. Data for the
  experimental treatment group in `nswdemo` are combined with the
  `psid1` control data from the Panel Study of Income Dynamics (PSID)
  study.

  This data frame contains the following columns:

  trt
      a numeric vector identifying the study in which the subjects were
      enrolled (0 = Control, 1 = treated).

  age
      age (in years).

  educ
      years of education.

  black
      (0 = not black, 1 = black).

  hisp
      (0 = not hispanic, 1 = hispanic).

  marr
      (0 = not married, 1 = married).

  nodeg
      (0 = completed high school, 1 = dropout).

  re74
      real earnings in 1974.

  re75
      real earnings in 1975.

  re78
      real earnings in 1978.

  http://www.nber.org/~rdehejia/nswdata.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nswpsid1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2787 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nswpsid1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nswpsid1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nswpsid1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
