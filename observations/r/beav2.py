# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def beav2(path):
  """Body Temperature Series of Beaver 2

  Reynolds (1994) describes a small part of a study of the long-term
  temperature dynamics of beaver *Castor canadensis* in north-central
  Wisconsin. Body temperature was measured by telemetry every 10 minutes
  for four females, but data from a one period of less than a day for each
  of two animals is used there.

  The `beav2` data frame has 100 rows and 4 columns. This data frame
  contains the following columns:

  `day`
      Day of observation (in days since the beginning of 1990), November
      3–4.

  `time`
      Time of observation, in the form `0330` for 3.30am.

  `temp`
      Measured body temperature in degrees Celsius.

  `activ`
      Indicator of activity outside the retreat.

  P. S. Reynolds (1994) Time-series analyses of beaver body temperatures.
  Chapter 11 of Lange, N., Ryan, L., Billard, L., Brillinger, D.,
  Conquest, L. and Greenhouse, J. eds (1994) *Case Studies in Biometry.*
  New York: John Wiley and Sons.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `beav2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'beav2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/beav2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='beav2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
