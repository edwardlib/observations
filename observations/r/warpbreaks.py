# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def warpbreaks(path):
  """The Number of Breaks in Yarn during Weaving

  This data set gives the number of warp breaks per loom, where a loom
  corresponds to a fixed length of yarn.

  A data frame with 54 observations on 3 variables.

+------------+---------------+-----------+----------------------------------+
| `[,1]`   | `breaks`    | numeric   | The number of breaks             |
+------------+---------------+-----------+----------------------------------+
| `[,2]`   | `wool`      | factor    | The type of wool (A or B)        |
+------------+---------------+-----------+----------------------------------+
| `[,3]`   | `tension`   | factor    | The level of tension (L, M, H)   |
+------------+---------------+-----------+----------------------------------+

  There are measurements on 9 looms for each of the six types of warp
  (`AL`, `AM`, `AH`, `BL`, `BM`, `BH`).

  Tippett, L. H. C. (1950) *Technological Applications of Statistics*.
  Wiley. Page 106.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `warpbreaks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 54 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'warpbreaks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/warpbreaks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='warpbreaks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
