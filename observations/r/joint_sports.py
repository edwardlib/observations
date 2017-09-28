# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def joint_sports(path):
  """Opinions About Joint Sports

  Data from a Danish study in 1983 and 1985 about sports activities and
  the opinion about joint sports with the other gender among 16–19 year
  old high school students.

  A data frame with 40 observations and 5 variables.

  Freq
      frequency.

  opinion
      factor indicating opinion about sports joint with the other gender
      (very good, good, indifferent, bad, very bad).

  year
      factor indicating year of study (1983, 1985).

  grade
      factor indicating school grade (1st, 3rd).

  gender
      factor indicating gender (Boy, Girl).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  page 210.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `joint_sports.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'joint_sports.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/JointSports.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='joint_sports.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
