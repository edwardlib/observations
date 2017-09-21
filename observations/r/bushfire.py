# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bushfire(path):
  """Campbell Bushfire Data

  This data set was used by Campbell (1984) to locate bushfire scars. The
  dataset contains satelite measurements on five frequency bands,
  corresponding to each of 38 pixels.

  A data frame with 38 observations on 5 variables.

  Maronna, R.A. and Yohai, V.J. (1995) The Behavoiur of the Stahel-Donoho
  Robust Multivariate Estimator. *Journal of the American Statistical
  Association* **90**, 330–341.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bushfire.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bushfire.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/robustbase/bushfire.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bushfire.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
