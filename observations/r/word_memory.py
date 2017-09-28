# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def word_memory(path):
  """WordMemory

  Percentage of different types of words recalled

  A dataset with 40 observations on the following 4 variables.

  `Subject`

  Code to identify each subject: `A` to `J`

  `Abstract`

  Words were abstract? `No` or `Yes`

  `Frequent`

  Words were common? `No` or `Yes`

  `Percent`

  Percentage of words recalled (out of 25)

  Data from a student laboratory project, Department of Psychology and

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `word_memory.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'word_memory.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/WordMemory.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='word_memory.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
