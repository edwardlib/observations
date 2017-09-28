# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def harman_8(path):
  """Correlations of eight physical variables (from Harman, 1966)

  A classic data set from Harman (1976) reporting the correlations of
  eight physical variables. Used by Harman for demonstrations of factor
  analysis (both principal axis and minimum residual).

  The format is: num [1:8, 1:8] 1 0.846 0.805 0.859 0.473 0.398 0.301
  0.382 0.846 1 ... - attr(\*, "dimnames")=List of 2 ..$ : chr [1:8]
  "Height" "Arm span" "Length of forearm" "Length of lower leg" ... ..$ :
  chr [1:8] "V1" "V2" "V3" "V4" ...

  H. Harman and W.Jones. (1966) Factor analysis by minimizing residuals
  (minres). Psychometrika, 31(3):351-368.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `harman_8.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'harman_8.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Harman.8.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='harman_8.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
