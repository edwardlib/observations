# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kootenay(path):
  """Waterflow Measurements of Kootenay River in Libby and Newgate

  The original data set is the waterflow in January of the Kootenay river,
  measured at two locations, namely, Libby (Montana) and Newgate (British
  Columbia) for 13 consecutive years, 1931–1943.

  The data set is of mostly interest because it has been used as example
  in innumerous didactical situations about robust regression. To this
  end, one number (in observation 4) has been modified from the original
  data from originally 44.9 to 15.7 (here).

  A data frame with 13 observations on the following 2 variables.

  `Libby`
      a numeric vector

  `Newgate`
      a numeric vector

  Original Data, p.58f of Ezekiel and Fox (1959), *Methods of Correlation
  and Regression Analysis*. Wiley, N.Y.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kootenay.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 13 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kootenay.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/kootenay.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kootenay.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
