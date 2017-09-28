# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def coleman(path):
  """Coleman Data Set

  Contains information on 20 Schools from the Mid-Atlantic and New England
  States, drawn from a population studied by Coleman et al. (1966).
  Mosteller and Tukey (1977) analyze this sample consisting of
  measurements on six different variables, one of which will be treated as
  a responce.

  A data frame with 20 observations on the following 6 variables.

  `salaryP`
      staff salaries per pupil

  `fatherWc`
      percent of white-collar fathers

  `sstatus`
      socioeconomic status composite deviation: means for family size,
      family intactness, father's education, mother's education, and home
      items

  `teacherSc`
      mean teacher's verbal test score

  `motherLev`
      mean mother's educational level, one unit is equal to two school
      years

  `Y`
      verbal mean test score (y, all sixth graders)

  Author(s)
  ~~~~~~~~~

  Valentin Todorov

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection* Wiley, p.79, table 2.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `coleman.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'coleman.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/coleman.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='coleman.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
