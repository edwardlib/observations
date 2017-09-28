# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hawk_tail2(path):
  """HawkTail2

  Tail lengths for three hawk species

  A dataset with observations on the following 3 variables.

  `Tail_CH`

  Tail length (in mm) for a sample of Cooper's hawks

  `Tail_RT`

  Tail length (in mm) for a sample of Red-tailed hawks

  `Tail_SS`

  Tail length (in mm) for a sample of Sharp-shinned hawks


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hawk_tail2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 577 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hawk_tail2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/HawkTail2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hawk_tail2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
