# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chemo_thc(path):
  """ChemoTHC

  Comparison of two treatments for nausea in chemotherapy

  A dataset with 2 observations on the following 4 variables.

  `Drug`

  `Prochlorperazine` or `THC`

  `Effective`

  Count of effectrive cases

  `NotEffective`

  Count of noneffective cases

  `Patients`

  Number of patients in the treatment

  Sallan SE, Cronin C, Zelen M, Zinberg NE (1980), "Antiemetics in
  patients receiving chemotherapy for cancer: a randomized comparison of
  delta-9-tetrahydrocannabinol and prochlorperazine," New England Journal

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chemo_thc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chemo_thc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/ChemoTHC.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chemo_thc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
