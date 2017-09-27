# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def intersalt(path):
  """Blood pressure versus Salt; inter-population data

  Median blood pressure, as a fuction of salt intake, for each of 52 human
  populations.

  A data frame with 52 observations on the following 4 variables.

  `b`
      a numeric vector

  `bp`
      mean diastolic blood pressure (mm Hg)

  `na`
      mean sodium excretion (mmol/24h)

  `country`
      a character vector

  Intersalt Cooperative Research Group. 1988. Intersalt: an international
  study of electrolyte excretion and blood pressure: results for 24 hour
  urinary sodium and potassium excretion. *British Medical Journal* 297:
  319-328.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `intersalt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 52 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'intersalt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/intersalt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='intersalt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
