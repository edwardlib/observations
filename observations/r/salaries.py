# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def salaries(path):
  """Salaries for Professors

  The 2008-09 nine-month academic salary for Assistant Professors,
  Associate Professors and Professors in a college in the U.S. The data
  were collected as part of the on-going effort of the college's
  administration to monitor salary differences between male and female
  faculty members.

  A data frame with 397 observations on the following 6 variables.

  `rank`
      a factor with levels `AssocProf` `AsstProf` `Prof`

  `discipline`
      a factor with levels `A` (“theoretical” departments) or `B`
      (“applied” departments).

  `yrs.since.phd`
      years since PhD.

  `yrs.service`
      years of service.

  `sex`
      a factor with levels `Female` `Male`

  `salary`
      nine-month salary, in dollars.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `salaries.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 397 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'salaries.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Salaries.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='salaries.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
