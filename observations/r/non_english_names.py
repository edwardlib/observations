# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def non_english_names(path):
  """Names with Character Set Problems

  A `data.frame` describing names containing character codes rare or
  non-existent in standard English text, e.g., with various accent marks
  that may not be coded consistenty in different locales or by different
  software.

  A `data.frame` with two columns:

  nonEnglish
      a character vector containing names that often have non-standard
      characters with the non-standard characters replaced by "\_"

  English
      a character vector containing a standard English-character
      translation of `nonEnglish`

  See Also
  ~~~~~~~~

  `grepNonStandardCharacters`, `subNonStandardCharacters`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `non_english_names.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'non_english_names.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/nonEnglishNames.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='non_english_names.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
