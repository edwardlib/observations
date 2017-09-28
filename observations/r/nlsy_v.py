# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nlsy_v(path):
  """National Longitudinal Survey of Youth Extract

  This dataset pertains to children and their families in the United
  States and is intended to illustrate missing data issues. Note that
  although the original data are longitudinal, this extract is not.

  A data frame with 400 randomly subsampled observations on the following
  7 variables.

  `ppvtr.36`
      a numeric vector with data on the Peabody Picture Vocabulary Test
      (Revised) administered at 36 months

  `first`
      indicator for whether child was first-born

  `b.marr`
      indicator for whether mother was married when child was born

  `income`
      a numeric vector with data on family income in year after the child
      was born

  `momage`
      a numeric vector with data on the age of the mother when the child
      was born

  `momed`
      educational status of mother when child was born (1 = less than high
      school, 2 = high school graduate, 3 = some college, 4 = college
      graduate)

  `momrace`
      race of mother (1 = black, 2 = Hispanic, 3 = white)

  Note that **momed** would typically be an ordered `factor` while
  **momrace** would typically be an unorderd `factor` but both are
  `numeric` in this `data.frame` in order to illustrate the mechanism
  to `change` the type of a `missing_variable`

  National Longitudinal Survey of Youth, 1997,
  http://www.bls.gov/nls/nlsy97.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nlsy_v.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 400 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nlsy_v.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mi/nlsyV.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nlsy_v.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
