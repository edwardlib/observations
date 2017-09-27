# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aspirin(path):
  """Aspirin Data

  Efficacy of Aspirin in preventing death after a myocardial infarct.

  A data frame with 7 observations on the following 4 variables.

  `dp`
      number of deaths after placebo.

  `tp`
      total number subjects treated with placebo.

  `da`
      number of deaths after Aspirin.

  `ta`
      total number of subjects treated with Aspirin.

  J. L. Fleiss (1993), The statistical basis of meta-analysis.
  *Statistical Methods in Medical Research* **2**, 121–145.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aspirin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aspirin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/aspirin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aspirin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
