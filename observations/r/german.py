# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def german(path):
  """German credit scoring data

  See website for details of data attributes

  A data frame with 1000 observations on the following 21 variables.

  `V1`
      a factor with levels `A11` `A12` `A13` `A14`

  `V2`
      a numeric vector

  `V3`
      a factor with levels `A30` `A31` `A32` `A33` `A34`

  `V4`
      a factor with levels `A40` `A41` `A410` `A42` `A43`
      `A44` `A45` `A46` `A48` `A49`

  `V5`
      a numeric vector

  `V6`
      a factor with levels `A61` `A62` `A63` `A64` `A65`

  `V7`
      a factor with levels `A71` `A72` `A73` `A74` `A75`

  `V8`
      a numeric vector

  `V9`
      a factor with levels `A91` `A92` `A93` `A94`

  `V10`
      a factor with levels `A101` `A102` `A103`

  `V11`
      a numeric vector

  `V12`
      a factor with levels `A121` `A122` `A123` `A124`

  `V13`
      a numeric vector

  `V14`
      a factor with levels `A141` `A142` `A143`

  `V15`
      a factor with levels `A151` `A152` `A153`

  `V16`
      a numeric vector

  `V17`
      a factor with levels `A171` `A172` `A173` `A174`

  `V18`
      a factor with levels `good` `bad`

  `V19`
      a factor with levels `A191` `A192`

  `V20`
      a factor with levels `A201` `A202`

  `V21`
      a numeric vector

  http://archive.ics.uci.edu/ml/datasets.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `german.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1000 rows and 21 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'german.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gamclass/german.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='german.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
