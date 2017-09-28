# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def harman_5(path):
  """5 socio-economic variables from Harman (1967)

  Harman (1967) uses 5 socio-economic variables for demonstrations of
  principal components and factor analysis. This example is used in the
  SAS manual for Proc Factor as well.

  A data frame with 12 observations on the following 5 variables.

  `population`
      a numeric vector

  `schooling`
      a numeric vector

  `employment`
      a numeric vector

  `professional`
      a numeric vector

  `housevalue`
      a numeric vector

  Harman, Harry Horace (1967), Modern factor analysis. Chicago, University
  of Chicago Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `harman_5.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'harman_5.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Harman.5.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='harman_5.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
