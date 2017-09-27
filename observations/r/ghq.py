# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ghq(path):
  """General Health Questionnaire

  Data from an psychiatric screening questionnaire

  A data frame with 22 observations on the following 4 variables.

  `GHQ`
      the General Health Questionnaire score.

  `sex`
      a factor with levels `female` and `male`

  `cases`
      the number of diseased subjects.

  `non.cases`
      the number of healthy subjects.

  D. Goldberg (1972). *The Detection of Psychiatric Illness by
  Questionnaire*, Oxford University Press, Oxford, UK.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ghq.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ghq.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/GHQ.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ghq.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
