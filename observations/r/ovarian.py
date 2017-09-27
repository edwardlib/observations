# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ovarian(path):
  """Ovarian Cancer Survival Data

  Survival in a randomised trial comparing two treatments for ovarian
  cancer

  futime:

  survival or censoring time

  fustat:

  censoring status

  age:

  in years

  resid.ds:

  residual disease present (1=no,2=yes)

  rx:

  treatment group

  ecog.ps:

  ECOG performance status (1 is better, see reference)

  Terry Therneau

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ovarian.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ovarian.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/ovarian.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ovarian.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
