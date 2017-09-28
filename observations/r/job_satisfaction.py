# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def job_satisfaction(path):
  """Job Satisfaction Data

  Data from Petersen (1968) about the job satisfaction of 715 blue collar
  workers, selected from Danish Industry in 1968.

  A data frame with 8 observations and 4 variables.

  Freq
      frequency.

  management
      factor indicating quality of management (bad, good).

  supervisor
      factor indicating supervisor's job satisfaction (low, high).

  own
      factor indicating worker's own job satisfaction (low, high).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  Table 5.4.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `job_satisfaction.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'job_satisfaction.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/JobSatisfaction.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='job_satisfaction.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
