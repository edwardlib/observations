# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def schizophrenia(path):
  """Age of Onset of Schizophrenia Data

  Data on sex differences in the age of onset of schizophrenia.

  A data frame with 251 observations on the following 2 variables.

  `age`
      age at the time of diagnosis.

  `gender`
      a factor with levels `female` and `male`

  E. Kraepelin (1919), *Dementia Praecox and Paraphrenia*. Livingstone,
  Edinburgh.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `schizophrenia.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 251 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'schizophrenia.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/schizophrenia.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='schizophrenia.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
