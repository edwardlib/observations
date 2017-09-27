# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ced_data(path):
  """Example Data for the Crossover Encouragement Design

  A randomly generated dataset containing 2000 rows and 7 columns with no
  missing values.

  A data frame containing the following variables, which are interpreted
  as results from a hypothetical randomized trial employing the crossover
  encouragement design.

  T1:
      The binary treatment indicator in the first stage.

  M1:
      The binary mediator variable recorded in the first stage.

  Y1:
      The binary outcome variable recorded in the first stage.

  T2:
      The binary treatment in the second stage. Equal to 1 - T1 by design.

  Z:
      The binary encouragement indicator for the second stage.

  M2:
      The binary mediator recorded in the second stage.

  Y2:
      The binary outcome recorded in the second stage.

  Imai, K., Tingley, D. and Yamamoto, T. (2012) Experimental Designs for
  Identifying Causal Mechanisms. Journal of the Royal Statistical Society,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ced_data.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2000 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ced_data.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mediation/CEDdata.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ced_data.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
