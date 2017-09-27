# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def respdis(path):
  """Clustered Ordinal Respiratory Disorder

  The `respdis` data frame has 111 rows and 3 columns. The study
  described in Miller et. al. (1993) is a randomized clinical trial of a
  new treatment of respiratory disorder. The study was conducted in 111
  patients who were randomly assigned to one of two treatments (active,
  placebo). At each of four visits during the follow-up period, the
  response status of each patients was classified on an ordinal scale.

  This data frame contains the following columns:

  y1, y2, y3, y4
      ordered factor measured at 4 visits for the response with levels,
      `1` < `2` < `3`, 1 = poor, 2 = good, and 3 = excellent

  trt
      a factor for treatment with levels, 1 = active, 0 = placebo.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `respdis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 111 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'respdis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/geepack/respdis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='respdis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
