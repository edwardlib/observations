# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lbwgrp(path):
  """lbwgrp

  grouped format of the lbw data. The observation level data come to us
  form Hosmer and Lemeshow (2000). Grouping is such that lowbw is the
  numerator, and cases the denominator of a binomial model, or cases may
  be an offset to the count variable, lowbw. Birthweights under 2500g
  classifies a low birthweight baby.

  A data frame with 6 observations on the following 7 variables.

  `lowbw`
      Number of low weight babies per covariate pattern: 12-60

  `cases`
      Number of observations with same covariate pattern: 30-165

  `smoke`
      1=history of mother smoking; 0=mother nonsmoker

  `race1`
      (1/0): Caucasian

  `race2`
      (1/0): Black

  `race3`
      (1/0): Other

  `low`
      low birth weight (not valid variable in grouped format)

  Hosmer, D and S. Lemeshow (2000), Applied Logistic Regression, Wiley

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lbwgrp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lbwgrp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/lbwgrp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lbwgrp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
