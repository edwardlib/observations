# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def blackmore(path):
  """Exercise Histories of Eating-Disordered and Control Subjects

  The `Blackmore` data frame has 945 rows and 4 columns. Blackmore and
  Davis's data on exercise histories of 138 teenaged girls hospitalized
  for eating disorders and 98 control subjects.

  This data frame contains the following columns:

  subject
      a factor with subject id codes.

  age
      age in years.

  exercise
      hours per week of exercise.

  group
      a factor with levels: `control`, Control subjects; `patient`,
      Eating-disordered patients.

  Personal communication from Elizabeth Blackmore and Caroline Davis, York

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `blackmore.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 945 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'blackmore.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Blackmore.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='blackmore.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
