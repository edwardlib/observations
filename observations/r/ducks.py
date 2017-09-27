# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ducks(path):
  """Behavioral and Plumage Characteristics of Hybrid Ducks

  The `ducks` data frame has 11 rows and 2 columns.

  Each row of the data frame represents a male duck who is a second
  generation cross of mallard and pintail ducks. For 11 such ducks a
  behavioural and plumage index were calculated. These were measured on
  scales devised for this experiment which was to examine whether there
  was any link between which species the ducks resembled physically and
  which they resembled in behaviour. The scale for the physical appearance
  ranged from 0 (identical in appearance to a mallard) to 20 (identical to
  a pintail). The behavioural traits of the ducks were on a scale from 0
  to 15 with lower numbers indicating closer to mallard-like in behaviour.

  This data frame contains the following columns:

  `plumage`
      The index of physical appearance based on the plumage of individual
      ducks.

  `behaviour`
      The index of behavioural characteristics of the ducks.

  The data were obtained from

  Larsen, R.J. and Marx, M.L. (1986) *An Introduction to Mathematical
  Statistics and its Applications* (Second Edition). Prentice-Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ducks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ducks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/ducks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ducks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
