# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cuckoos(path):
  """Cuckoo Eggs Data

  Length and breadth measurements of 120 eggs lain in the nests of six
  different species of host bird.

  This data frame contains the following columns:

  length
      the egg lengths in millimeters

  breadth
      the egg breadths in millimeters

  species
      a factor with levels `hedge.sparrow`, `meadow.pipit`,
      `pied.wagtail`, `robin`, `tree.pipit`, `wren`

  id
      a numeric vector

  Latter, O.H. (1902). The eggs of Cuculus canorus. An Inquiry into the
  dimensions of the cuckoo's egg and the relation of the variations to the
  size of the eggs of the foster-parent, with notes on coloration, &c.
  Biometrika i, 164.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cuckoos.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 120 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cuckoos.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/cuckoos.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cuckoos.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
