# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leukemia(path):
  """Acute Myelogenous Leukemia survival data

  Survival in patients with Acute Myelogenous Leukemia. The question at
  the time was whether the standard course of chemotherapy should be
  extended ('maintainance') for additional cycles.

  time:

  survival or censoring time

  status:

  censoring status

  x:

  maintenance chemotherapy given? (factor)

  Rupert G. Miller (1997), *Survival Analysis*. John Wiley & Sons. ISBN:

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leukemia.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leukemia.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/leukemia.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leukemia.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
