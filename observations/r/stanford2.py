# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def stanford2(path):
  """More Stanford Heart Transplant data

  This contains the Stanford Heart Transplant data in a different format.
  The main data set is in `heart`.

  id:

  ID number

  time:

  survival or censoring time

  status:

  censoring status

  age:

  in years

  t5:

  T5 mismatch score

  LA Escobar and WQ Meeker Jr (1992), Assessing influence in regression
  analysis with censored data. *Biometrics* **48**, 507–528. Page 519.

  See Also
  ~~~~~~~~


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `stanford2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 184 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'stanford2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/stanford2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='stanford2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
