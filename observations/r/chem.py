# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chem(path):
  """Copper in Wholemeal Flour

  A numeric vector of 24 determinations of copper in wholemeal flour, in
  parts per million.

  Analytical Methods Committee (1989) Robust statistics – how not to
  reject outliers. *The Analyst* **114**, 1693–1702.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chem.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chem.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/chem.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chem.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
