# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fa(path):
  """Friedreich Ataxia data

  This data set contains a case-control indicator and twelve
  microsatellite markers. An extra unphased individual with the following
  genotype

  ::

       2  7  7  7  1  3  2  2  2  2  6  3
       3  8 10  8  3  9  3  4  2  2  7  5

  has not been included.

  The inter-marker distances (Morgan) are as follows,

  0.03, 0.065, 0.00125, 0.00125, 0.00125, 0.00125, 0.00125, 0.00125,
  0.00125, 0.00125, 0.045

  A data frame containing 127 rows and 13 columns

  Liu JS, Sabatti C, Teng J, Keats BJB, Risch N (2001). Bayesian analysis
  of haplotypes for linkage disequilibrium mapping Genome Research

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fa.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 127 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fa.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/fa.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fa.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
