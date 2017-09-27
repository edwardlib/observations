# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dwyer(path):
  """8 cognitive variables used by Dwyer for an example.

  Dwyer (1937) introduced a technique for factor extension and used 8
  cognitive variables from Thurstone. This is the example data set used in
  his paper.

  The format is: num [1:8, 1:8] 1 0.58 -0.28 0.01 0.36 0.38 0.61 0.15 0.58
  1 ... - attr(\*, "dimnames")=List of 2 ..$ : chr [1:8] "V1" "V2" "V3"
  "V4" ... ..$ : chr [1:8] "V1" "V2" "V3" "V4" ...

  Data matrix retyped from the original publication.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dwyer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dwyer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Dwyer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dwyer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
