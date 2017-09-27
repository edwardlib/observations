# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nsw74psid3(path):
  """Labour Training Evaluation Data

  These data are pertinent to an investigation of the way that earnings
  changed, between 1974-1975 and 1978, in the absence of training. The
  data frame combines data for the experimental treatment group (NSW, 185
  observations), using as control data results from the PSID (Panel Study
  of Income Dynamics) study (128 observations). The latter were chosen to
  mimic the characteristics of the NSW training and control groups. These
  are a subset of the `nsw74psid1` data.

  This data frame contains the following columns:

  trt
      a numeric vector identifying the study in which the subjects were
      enrolled (0 = PSID, 1 = NSW)

  age
      age (in years)

  educ
      years of education

  black
      (0 = not black, 1 = black)

  hisp
      (0 = not hispanic, 1 = hispanic)

  marr
      (0 = not married, 1 = married)

  nodeg
      (0 = completed high school, 1 = dropout)

  re74
      real earnings in 1974

  re75
      real earnings in 1975

  re78
      real earnings in 1978

  http://www.columbia.edu/~rd247/nswdata.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nsw74psid3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 313 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nsw74psid3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nsw74psid3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nsw74psid3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
