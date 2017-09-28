# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sat_gpa(path):
  """SAT scores and GPA

  A sample of SAT scores and grade point averages for statistics students

  A dataset with 24 observations on the following 3 variables.

  `MathSAT`

  Score (out of 800) on the mathematics portion of the SAT exam

  `VerbalSAT`

  Score (out of 800) on the verbal portion of the SAT exam

  `GPA`

  Grade point average (0.0-4.0 scale)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sat_gpa.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sat_gpa.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/SATGPA.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sat_gpa.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
