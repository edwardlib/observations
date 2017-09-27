# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def transplant(path):
  """Liver transplant waiting list

  Subjects on a liver transplant waiting list from 1990-1999, and their
  disposition: received a transplant, died while waiting, withdrew from
  the list, or censored.

  A data frame with 815 observations on the following 6 variables.

  `age`
      age at addition to the waiting list

  `sex`
      `m` or `f`

  `abo`
      blood type: `A`, `B`, `AB` or `O`

  `year`
      year in which they entered the waiting list

  `futime`
      time from entry to final disposition

  `event`
      final disposition: `censored`, `death`, `ltx` or `withdraw`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `transplant.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 815 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'transplant.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/transplant.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='transplant.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
