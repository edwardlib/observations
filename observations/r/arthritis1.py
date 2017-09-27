# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def arthritis1(path):
  """Rheumatoid Arthritis Clinical Trial

  Rheumatoid self-assessment scores for 302 patients, measured on a
  five-level ordinal response scale at three follow-up times.

  A data frame with 906 observations on the following 7 variables:

  `id`
      Patient identifier variable.

  `y`
      Self-assessment score of rheumatoid arthritis measured on a
      five-level ordinal response scale.

  `sex`
      Coded as (1) for female and (2) for male.

  `age`
      Recorded at the baseline.

  `trt`
      Treatment group variable, coded as (1) for the placebo group and (2)
      for the drug group.

  `baseline`
      Self-assessment score of rheumatoid arthritis at the baseline.

  `time`
      Follow-up time recorded in months.

  Lipsitz, S.R. and Kim, K. and Zhao, L. (1994) Analysis of repeated
  categorical data using generalized estimating equations. *Statistics in
  Medicine*, **13**, 1149–1163.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `arthritis1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 906 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'arthritis1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/multgee/arthritis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='arthritis1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
