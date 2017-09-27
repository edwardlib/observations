# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def orchard_sprays(path):
  """Potency of Orchard Sprays

  An experiment was conducted to assess the potency of various
  constituents of orchard sprays in repelling honeybees, using a Latin
  square design.

  A data frame with 64 observations on 4 variables.

  +--------+-------------+-----------+------------------------+
  | [,1]   | rowpos      | numeric   | Row of the design      |
  +--------+-------------+-----------+------------------------+
  | [,2]   | colpos      | numeric   | Column of the design   |
  +--------+-------------+-----------+------------------------+
  | [,3]   | treatment   | factor    | Treatment level        |
  +--------+-------------+-----------+------------------------+
  | [,4]   | decrease    | numeric   | Response               |
  +--------+-------------+-----------+------------------------+

  Finney, D. J. (1947) *Probit Analysis*. Cambridge.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `orchard_sprays.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 64 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'orchard_sprays.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/OrchardSprays.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='orchard_sprays.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
