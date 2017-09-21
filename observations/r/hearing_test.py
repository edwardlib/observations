# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hearing_test(path):
  """HearingTest

  HearingTest

  A dataset with 96 observations on the following 3 variables.

  `Subj`

  Subject number (1 - 24)

  `List`

  List of words: `L1` `L2` `L3` `L4`

  `Percent`

  Percent (out of 50) of words correctly identified

  Data downloaded from DASL at
  http://lib.stat.cmu.edu/DASL/Datafiles/Hearing.html.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hearing_test.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 96 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hearing_test.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/Stat2Data/HearingTest.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hearing_test.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
