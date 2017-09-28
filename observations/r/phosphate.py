# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def phosphate(path):
  """Phosphate Level Data

  Plasma inorganic phosphate levels from 33 subjects.

  A data frame with 33 observations on the following 9 variables.

  `group`
      a factor with levels `control` and `obese`.

  `t0`
      baseline phosphate level

  ,

  `t0.5`
      phosphate level after 1/2 an hour.

  `t1`
      phosphate level after one an hour.

  `t1.5`
      phosphate level after 1 1/2 hours.

  `t2`
      phosphate level after two hours.

  `t3`
      phosphate level after three hours.

  `t4`
      phosphate level after four hours.

  `t5`
      phosphate level after five hours.

  C. S. Davis (2002), *Statistical Methods for the Analysis of Repeated
  Measurements*, Springer, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `phosphate.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 33 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'phosphate.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/phosphate.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='phosphate.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
