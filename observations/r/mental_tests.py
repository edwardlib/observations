# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mental_tests(path):
  """Six Mental Tests

  These data are from the SAS manual and consist of six mental tests for
  32 students, with some missing data. The three `x` variables are
  intended to load on a verbal factor, and the three `y` variables on a
  math factor. The data can be used to illustrate the estimation of a
  confirmatory factor analysis model by multinormal full-information
  maximum-likelihood in the presence of missing data.

  A data frame with 32 observations on the following 6 variables.

  `x1`
      score on verbal test 1.

  `x2`
      score on verbal test 2.

  `x3`
      score on verbal test 3.

  `y1`
      score on math test 1.

  `y2`
      score on math test 2.

  `y3`
      score on math test 3.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mental_tests.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mental_tests.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/sem/Tests.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mental_tests.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
