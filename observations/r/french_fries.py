# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def french_fries(path):
  """Sensory data from a french fries experiment.

  This data was collected from a sensory experiment conducted at Iowa
  State University in 2004. The investigators were interested in the
  effect of using three different fryer oils had on the taste of the
  fries.

  A data frame with 696 rows and 9 variables

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `french_fries.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 696 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'french_fries.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/reshape2/french_fries.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='french_fries.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
