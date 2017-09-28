# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def condroz(path):
  """Condroz Data

  Dataset with pH-value and Calcium content in soil samples, collected in
  different communities of the Condroz region in Belgium. The data pertain
  to a subset of 428 samples with a pH-value between 7.0 and 7.5.

  A data frame with 428 observations on the following 2 variables.

  `Ca`
      Calcium content of the soil sample

  `pH`
      pH value of the soil sample

  Hubert and Vandervieren (2006), p. 10. This dataset is also studied in
  Vandewalle et al. (2004).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `condroz.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 428 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'condroz.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/condroz.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='condroz.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
