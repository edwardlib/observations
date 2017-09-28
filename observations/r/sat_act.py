# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sat_act(path):
  """3 Measures of ability: SATV, SATQ, ACT

  Self reported scores on the SAT Verbal, SAT Quantitative and ACT were
  collected as part of the Synthetic Aperture Personality Assessment
  (SAPA) web based personality assessment project. Age, gender, and
  education are also reported. The data from 700 subjects are included
  here as a demonstration set for correlation and analysis.

  A data frame with 700 observations on the following 6 variables.

  `gender`
      males = 1, females = 2

  `education`
      self reported education 1 = high school ... 5 = graduate work

  `age`
      age

  `ACT`
      ACT composite scores may range from 1 - 36. National norms have a
      mean of 20.

  `SATV`
      SAT Verbal scores may range from 200 - 800.

  `SATQ`
      SAT Quantitative scores may range from 200 - 800

  http://personality-project.org

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sat_act.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 700 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sat_act.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/sat.act.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sat_act.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
