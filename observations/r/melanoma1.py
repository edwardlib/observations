# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def melanoma1(path):
  """Survival from Malignant Melanoma

  The `Melanoma` data frame has data on 205 patients in Denmark with
  malignant melanoma.

  This data frame contains the following columns:

  `time`
      survival time in days, possibly censored.

  `status`
      `1` died from melanoma, `2` alive, `3` dead from other causes.

  `sex`
      `1` = male, `0` = female.

  `age`
      age in years.

  `year`
      of operation.

  `thickness`
      tumour thickness in mm.

  `ulcer`
      `1` = presence, `0` = absence.

  P. K. Andersen, O. Borgan, R. D. Gill and N. Keiding (1993) *Statistical

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `melanoma1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 205 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'melanoma1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Melanoma.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='melanoma1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
