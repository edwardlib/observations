# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rh_dnase(path):
  """rhDNASE data set

  Results of a randomized trial of rhDNase for the treatment of cystic
  fibrosis.

  A data frame with 767 observations on the following 8 variables.

  `id`
      subject id

  `inst`
      enrolling institution

  `trt`
      treatment arm: 0=placebo, 1= rhDNase

  `entry.dt`
      date of entry into the study

  `end.dt`
      date of last follow-up

  `fev`
      forced expriatory volume at enrollment, a measure of lung capacity

  `ivstart`
      days from enrollment to the start of IV antibiotics

  `ivstop`
      days from enrollment to the cessation of IV antibiotics

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rh_dnase.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 767 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rh_dnase.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/rhDNase.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rh_dnase.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
