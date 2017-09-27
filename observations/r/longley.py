# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def longley(path):
  """Longley's Economic Regression Data

  A macroeconomic data set which provides a well-known example for a
  highly collinear regression.

  A data frame with 7 economical variables, observed yearly from 1947 to
  1962 (*n=16*).

  `GNP.deflator`
      GNP implicit price deflator (*1954=100*)

  `GNP`
      Gross National Product.

  `Unemployed`
      number of unemployed.

  `Armed.Forces`
      number of people in the armed forces.

  `Population`
      ‘noninstitutionalized’ population *≥* 14 years of age.

  `Year`
      the year (time).

  `Employed`
      number of people employed.

  The regression `lm(Employed ~ .)` is known to be highly collinear.

  J. W. Longley (1967) An appraisal of least-squares programs from the
  point of view of the user. *Journal of the American Statistical
  Association* **62**, 819–841.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `longley.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'longley.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/longley.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='longley.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
