# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def plasma(path):
  """Blood Screening Data

  The erythrocyte sedimentation rate and measurements of two plasma
  proteins (fibrinogen and globulin).

  A data frame with 32 observations on the following 3 variables.

  `fibrinogen`
      the fibrinogen level in the blood.

  `globulin`
      the globulin level in the blood.

  `ESR`
      the erythrocyte sedimentation rate, either less or greater 20 mm /
      hour.

  D. Collett and A. A. Jemain (1985), Residuals, outliers and influential
  observations in regression analysis. *Sains Malaysiana*, **4**, 493–511.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `plasma.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'plasma.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/plasma.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='plasma.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
