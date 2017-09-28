# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def within_between(path):
  """An example of the distinction between within group and between group corre
  lations

  A demonstration that a correlation may be decomposed to a within group
  correlation and a between group correlations and these two correlations
  are independent. Between group correlations are sometimes called
  ecological correlations, the decomposition into within and between group
  correlations is a basic concept in multilevel modeling. This data set
  shows the composite correlations between 9 variables, representing 16
  cases with four groups.

  A data frame with 16 observations on the following 10 variables.

  `Group`
      An example grouping factor.

  `V1`
      A column of 16 observations

  `V2`
      A column of 16 observations

  `V3`
      A column of 16 observations

  `V4`
      A column of 16 observations

  `V5`
      A column of 16 observations

  `V6`
      A column of 16 observations

  `V7`
      A column of 16 observations

  `V8`
      A column of 16 observations

  `V9`
      A column of 16 observations

  The data were created for this example

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `within_between.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'within_between.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/withinBetween.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='within_between.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
