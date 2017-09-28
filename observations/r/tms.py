# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tms(path):
  """TMS

  Effects of transcranial magnetic stimulation (TMS) on migraine headaches

  A dataset with 2 observations on the following 4 variables.

  `Group`

  Treatment group: `Placebo` or `TMS`

  `Yes`

  Count of number of patients that were pain-free

  `No`

  Count of number of patients that had pain

  `Trials`

  Number of patients in the group

  Based on results in R. B. Lipton, et. al. (2010) “Single-pulse
  Transcranial Magnetic Stimulation for Acute Treatment of Migraine with
  Aura: A Randomised, Double-blind, Parallel-group, Sham-controlled

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tms.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tms.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/TMS.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tms.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
