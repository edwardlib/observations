# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wage(path):
  """Mid-Atlantic Wage Data

  Wage and other data for a group of 3000 workers in the Mid-Atlantic
  region.

  A data frame with 3000 observations on the following 12 variables.

  `year`
      Year that wage information was recorded

  `age`
      Age of worker

  `sex`
      Gender

  `maritl`
      A factor with levels `1. Never Married` `2. Married`
      `3. Widowed` `4. Divorced` and `5. Separated` indicating
      marital status

  `race`
      A factor with levels `1. White` `2. Black` `3. Asian` and
      `4. Other` indicating race

  `education`
      A factor with levels `1. < HS Grad` `2. HS Grad`
      `3. Some College` `4. College Grad` and `5. Advanced Degree`
      indicating education level

  `region`
      Region of the country (mid-atlantic only)

  `jobclass`
      A factor with levels `1. Industrial` and `2. Information`
      indicating type of job

  `health`
      A factor with levels `1. <=Good` and `2. >=Very Good` indicating
      health level of worker

  `health_ins`
      A factor with levels `1. Yes` and `2. No` indicating whether
      worker has health insurance

  `logwage`
      Log of workers wage

  `wage`
      Workers raw wage

  Data was manually assembled by Steve Miller, of Open BI
  (www.openbi.com), from the March 2011 Supplement to Current Population
  Survey data.

  http://thedataweb.rm.census.gov/TheDataWeb

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wage.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3000 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wage.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Wage.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wage.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
