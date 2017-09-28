# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def whickham(path):
  """Data from the Whickham survey

  Data on age, smoking, and mortality from a one-in-six survey of the
  electoral roll in Whickham, a mixed urban and rural district near
  Newcastle upon Tyne, in the UK. The survey was conducted in 1972-1974 to
  study heart disease and thyroid disease. A follow-up on those in the
  survey was conducted twenty years later.

  A data frame with 1314 observations on women for the following
  variables.

  -  `outcome` survival status after 20 years: a factor with levels
     `Alive` `Dead`

  -  `smoker` smoking status at baseline: a factor with levels `No`
     `Yes`

  -  `age` age (in years) at the time of the first survey

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `whickham.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1314 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'whickham.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Whickham.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='whickham.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
