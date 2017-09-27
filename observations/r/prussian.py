# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def prussian(path):
  """Prussian army horse kick data

  Deaths by year, by corp, from horse kicks.

  A data frame with 280 observations on the following 3 variables.

  `y`
      a numeric vector, count of deaths

  `year`
      a numeric vector, 18XX, year of observation

  `corp`
      a `factor`, corp of Prussian Army generating observation

  von Bortkiewicz, L. 1898. *Das Gesetz der Kleinen Zahlen.* Leipzig:
  Teubner.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `prussian.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 280 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'prussian.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/prussian.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='prussian.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
