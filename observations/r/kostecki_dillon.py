# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kostecki_dillon(path):
  """Treatment of Migraine Headaches

  Subset of data on migraine treatments collected by Tammy
  Kostecki-Dillon.

  A data frame with 4152 observations on 133 subjects for the following 9
  variables.

  `id`
      Patient id.

  `time`
      time in days relative to the onset of treatment, which occurs at
      time 0.

  `dos`
      time in days from the start of the study, January 1 of the first
      year of the study.

  `hatype`
      a factor with levels `Aura` `Mixed` `No Aura`, the type of
      migraine experienced by a subject.

  `age`
      at onset of treatment, in years.

  `airq`
      a measure of air quality.

  `medication`
      a factor with levels `none` `reduced` `continuing`,
      representing subjects who discontinued their medication, who
      continued but at a reduced dose, or who continued at the previous
      dose.

  `headache`
      a factor with levels `no` `yes`.

  `sex`
      a factor with levels `female` `male`.

  Personal communication from Georges Monette (and adapted from his
  description of the data).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kostecki_dillon.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4152 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kostecki_dillon.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/KosteckiDillon.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kostecki_dillon.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
