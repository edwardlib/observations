# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def boundsdata(path):
  """Example Data for the Design Functions

  A random subsample of the simulated data used in Imai, Tingley, Yamamoto
  (2012). The data contains 1000 rows and 7 columns with no missing
  values.

  A data frame containing the following variables, which are interpreted
  as results from a hypothetical randomized trial. See the source for a
  full description.

  out:
      The binary outcome variable under the parallel design.

  out.enc:
      The binary outcome variable under the parallel encouragement design.

  med:
      The binary mediator under the parallel design.

  med.enc:
      The binary mediator under the parallel encouragement design.

  ttt:
      The binary treatment variable.

  manip:
      The design indicator, or the variable indicating whether the
      mediator is manipulated under the parallel design.

  enc:
      The trichotomous encouragement variable under the parallel
      encouragement design. Equals 0 if subject received no encouragement;
      1 if encouraged for the mediator value of 1; and -1 if encouraged
      for the mediator value of 0.

  Imai, K., Tingley, D. and Yamamoto, T. (2012) Experimental Designs for
  Identifying Causal Mechanisms. Journal of the Royal Statistical Society,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `boundsdata.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1000 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'boundsdata.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mediation/boundsdata.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='boundsdata.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
