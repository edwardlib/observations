# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def foodstamp(path):
  """Food Stamp Program Participation

  This data consists of 150 randomly selected persons from a survey with
  information on over 2000 elderly US citizens, where the response,
  indicates participation in the U.S. Food Stamp Program.

  A data frame with 150 observations on the following 4 variables.

  `participation`
      participation in U.S. Food Stamp Program; yes = 1, no = 0

  `tenancy`
      tenancy, indicating home ownership; yes = 1, no = 0

  `suppl.income`
      supplemental income, indicating whether some form of supplemental
      security income is received; yes = 1, no = 0

  `income`
      monthly income (in US dollars)

  Data description and first analysis: Stefanski et al.(1986) who indicate
  Rizek(1978) as original source of the larger study.

  Electronic version from CRAN package catdata.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `foodstamp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 150 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'foodstamp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/foodstamp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='foodstamp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
