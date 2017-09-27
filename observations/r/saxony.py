# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def saxony(path):
  """Families in Saxony

  Data from Geissler, cited in Sokal & Rohlf (1969) and Lindsey (1995) on
  gender distributions in families in Saxony in the 19th century.

  A 1-way table giving the number of male children in 6115 families of
  size 12. The variable and its levels are

  No

  Name

  Levels

  1

  nMales

  0, 1, ..., 12

  M. Friendly (2000), Visualizing Categorical Data, pages 40–42.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `saxony.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 13 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'saxony.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Saxony.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='saxony.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
