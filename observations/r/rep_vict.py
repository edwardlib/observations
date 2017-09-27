# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rep_vict(path):
  """Repeat Victimization Data

  Data from Reiss (1980) given by Fienberg (1980) about instances of
  repeat victimization for households in the U.S. National Crime Survey.

  A 2-dimensional array resulting from cross-tabulating victimization. The
  variables and their levels are as follows:

+---------------------+--------------------------+--------------------------+
| No                  | Name                     | Levels                   |
+---------------------+--------------------------+--------------------------+
| 1                   | First Victimization      | Rape, Assault, Robbery,  |
|                     |                          | Pickpocket, Personal     |
|                     |                          | Larceny,                 |
+---------------------+--------------------------+--------------------------+
|                     |                          | Burglary, Household      |
|                     |                          | Larceny, Auto Theft      |
+---------------------+--------------------------+--------------------------+
| 2                   | Second Victimization     | Rape, Assault, Robbery,  |
|                     |                          | Pickpocket, Personal     |
|                     |                          | Larceny,                 |
+---------------------+--------------------------+--------------------------+
|                     |                          | Burglary, Household      |
|                     |                          | Larceny, Auto Theft      |
+---------------------+--------------------------+--------------------------+

  Michael Friendly (2000), Visualizing Categorical Data, page 113.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rep_vict.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rep_vict.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/RepVict.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rep_vict.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
