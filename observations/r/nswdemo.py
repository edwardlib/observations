# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nswdemo(path):
  """Labour Training Evaluation Data

  The `nswdemo` data frame contains 722 rows and 10 columns. These data
  are pertinent to an investigation of the way that earnings changed,
  between 1974-1975 and 1978, for an experimental treatment who were given
  job training as compared with a control group who did not receive such
  training.

  The `psid1` data set is an alternative non-experimental "control"
  group. `psid2` and `psid3` are subsets of `psid1`, designed to be
  better matched to the experimental data than `psid1`. Note also the
  `cps1`, `cps2` and `cps3` datasets (DAAGxtras) that have been
  proposed as non-experimental controls.

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
      Filename is `nswdemo.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 722 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nswdemo.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nswdemo.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nswdemo.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
