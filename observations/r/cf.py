# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cf(path):
  """Cystic fibrosis data

  This data set contains a case-control indicator and 23 SNPs.

  The inter-marker distances (Morgan) are as follows

  0.000090, 0.000158, 0.005000, 0.000100, 0.000200, 0.000150, 0.000250,
  0.000200, 0.000050, 0.000350, 0.000300, 0.000250, 0.000350, 0.000350,
  0.000800, 0.000100, 0.000200, 0.000150, 0.000550, 0.006000, 0.000700,
  0.001000

  A data frame containing 186 rows and 24 columns

  Liu JS, Sabatti C, Teng J, Keats BJB, Risch N (2001). Bayesian Analysis
  of Haplotypes for Linkage Disequilibrium Mapping. Genome Research

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cf.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 186 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cf.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/cf.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cf.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
