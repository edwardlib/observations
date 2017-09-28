# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cars93_summary(path):
  """A Summary of the Cars93 Data set

  The `Cars93.summary` data frame has 6 rows and 4 columns created from
  information in the `Cars93` data set in the Venables and Ripley MASS
  package. Each row corresponds to a different class of car (e.g. Compact,
  Large, etc.).

  This data frame contains the following columns:

  Min.passengers
      minimum passenger capacity for each class of car

  Max.passengers
      maximum passenger capacity for each class of car

  No.of.cars
      number of cars in each class

  abbrev
      a factor with levels `C` Compact, `L` Large, `M` Mid-Size,
      `Sm` Small, `Sp` Sporty, `V` Van

  Lock, R. H. (1993) 1993 New Car Data. Journal of Statistics Education
  1(1)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cars93_summary.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cars93_summary.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/Cars93.summary.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cars93_summary.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
