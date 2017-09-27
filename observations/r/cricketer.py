# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cricketer(path):
  """Lifespans of UK 1st class cricketers born 1840-1960

  Year and birth, lifespan, etc, of British first class cricketers, born
  1840-1960, whose handedness could be determined from information in the
  Who's who of cricketers. The status (alive=0, dead =1), and lifetime or
  lifespan, is for 1992.

  A data frame with 5960 observations on the following 8 variables.

  `left`
      a factor with levels `right` `left`

  `year`
      numeric, year of birth

  `life`
      numeric, lifetime or lifespan to 1992

  `dead`
      numeric (0 = alive (censored), 1 = dead, in 1992)

  `acd`
      numeric (0 = not accidental or not dead, 1 = accidental death)

  `kia`
      numeric (0 = not killed in action, 1 = killed in action)

  `inbed`
      numeric (0 = did not die in bed, 1 = died in bed)

  `cause`
      a factor with levels `alive` `acd` (accidental death) `inbed`
      (died in bed)

  John Aggleton, Martin Bland. Data were collated as described in Aggleton
  et al.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cricketer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5960 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cricketer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/cricketer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cricketer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
