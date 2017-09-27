# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vince111b(path):
  """Averages by block of corn yields, for treatment 111 only

  These data frames have averages by blocks (parcels) for the treatment
  `111`.

  A data frame with 36 observations on 8 variables.

  site
      a factor with levels `AGSV` `CASV` `CPSV` `LPSV` `MPSV`
      `OOSV` `OTSV` `SSSV` `UISV`

  parcel
      a factor with levels `I` `II` `III` `IV`

  code
      a numeric vector

  island
      a numeric vector

  id
      a numeric vector

  plot
      a numeric vector

  trt
      a numeric vector

  harvwt
      a numeric vector

  Andrews DF; Herzberg AM, 1985. Data. A Collection of Problems from Many
  Fields for the Student and Research Worker. Springer-Verlag. (pp.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vince111b.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vince111b.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/vince111b.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vince111b.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
