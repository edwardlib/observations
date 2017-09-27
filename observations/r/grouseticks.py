# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grouseticks(path):
  """Data on red grouse ticks from Elston et al. 2001

  Number of ticks on the heads of red grouse chicks sampled in the field
  (`grouseticks`) and an aggregated version (`grouseticks_agg`); see
  original source for more details

  `INDEX`
      (factor) chick number (observation level)

  `TICKS`
      number of ticks sampled

  `BROOD`
      (factor) brood number

  `HEIGHT`
      height above sea level (meters)

  `YEAR`
      year (-1900)

  `LOCATION`
      (factor) geographic location code

  `cHEIGHT`
      centered height, derived from `HEIGHT`

  `meanTICKS`
      mean number of ticks by brood

  `varTICKS`
      variance of number of ticks by brood

  Robert Moss, via David Elston

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grouseticks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 403 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grouseticks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/grouseticks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grouseticks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
