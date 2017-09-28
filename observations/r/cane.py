# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cane(path):
  """Sugar-cane Disease Data

  The `cane` data frame has 180 rows and 5 columns. The data frame
  represents a randomized block design with 45 varieties of sugar-cane and
  4 blocks.

  This data frame contains the following columns:

  `n`
      The total number of shoots in each plot.

  `r`
      The number of diseased shoots.

  `x`
      The number of pieces of the stems, out of 50, planted in each plot.

  `var`
      A factor indicating the variety of sugar-cane in each plot.

  `block`
      A factor for the blocks.

  The data were kindly supplied by Dr. C.G.B. Demetrio of Escola Superior
  de Agricultura, Universidade de Sao Paolo, Brazil.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cane.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 180 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cane.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/cane.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cane.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
