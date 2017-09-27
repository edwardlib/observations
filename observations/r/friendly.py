# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def friendly(path):
  """Format Effects on Recall

  The `Friendly` data frame has 30 rows and 2 columns. The data are from
  an experiment on subjects' ability to remember words based on the
  presentation format.

  This data frame contains the following columns:

  condition
      A factor with levels: `Before`, Recalled words presented before
      others; `Meshed`, Recalled words meshed with others; `SFR`,
      Standard free recall.

  correct
      Number of words correctly recalled, out of 40 on final trial of the
      experiment.

  Friendly, M. and Franklin, P. (1980) Interactive presentation in
  multitrial free recall. *Memory and Cognition* **8** 265–270 [Personal
  communication from M. Friendly].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `friendly.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'friendly.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Friendly.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='friendly.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
