# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ucb_admissions(path):
  """Student Admissions at UC Berkeley

  Aggregate data on applicants to graduate school at Berkeley for the six
  largest departments in 1973 classified by admission and sex.

  A 3-dimensional array resulting from cross-tabulating 4526 observations
  on 3 variables. The variables and their levels are as follows:

  +------+----------+----------------------+
  | No   | Name     | Levels               |
  +------+----------+----------------------+
  | 1    | Admit    | Admitted, Rejected   |
  +------+----------+----------------------+
  | 2    | Gender   | Male, Female         |
  +------+----------+----------------------+
  | 3    | Dept     | A, B, C, D, E, F     |
  +------+----------+----------------------+

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ucb_admissions.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ucb_admissions.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/UCBAdmissions.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ucb_admissions.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
