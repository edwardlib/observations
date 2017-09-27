# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def brambles(path):
  """Spatial Location of Bramble Canes

  The `brambles` data frame has 823 rows and 3 columns.

  The location of living bramble canes in a 9m square plot was recorded.
  We take 9m to be the unit of distance so that the plot can be thought of
  as a unit square. The bramble canes were also classified by their age.

  This data frame contains the following columns:

  `x`
      The x coordinate of the position of the cane in the plot.

  `y`
      The y coordinate of the position of the cane in the plot.

  `age`
      The age classification of the canes; `0` indicates a newly emerged
      cane, `1` indicates a one year old cane and `2` indicates a two
      year old cane.

  The data were obtained from

  Diggle, P.J. (1983) *Statistical Analysis of Spatial Point Patterns*.
  Academic Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `brambles.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 823 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'brambles.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/brambles.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='brambles.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
