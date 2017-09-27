# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def election08(path):
  """Election08

  State-by-state information from the 2008 U.S. presidential election

  A dataset with 51 observations on the following 7 variables.

  `State`

  Name of the state

  `Abr`

  Abbreviation for the state

  `Income`

  Per capita income in the state as of 2007 (in dollars)

  `HS`

  Percentage of adults with at least a high school education

  `BA`

  Percentage of adults with at least a college education

  `Dem.Rep`

  Difference in %Democrat-%Republican (according to 2008 Gallup survey)

  `ObamaWin`

  `1`\ = Obama (Democrat) wins state in 2008 or `0`\ =McCain
  (Republican wins)

  | State income data from: Census Bureau Table 659. Personal INcome Per
    Capita (in 2007)
  | High school data from: U.S. Census Bureau, 1990 Census of Population,
    http://nces.ed.gov/programs/digest/d08/tables/dt08\_011.asp
  | College data from: Census Bureau Table 225. Educational Attainment by
    State (in 2007)
  | % Democrat and % Republican:

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `election08.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'election08.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Election08.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='election08.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
