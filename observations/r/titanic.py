# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def titanic(path):
  """Survival of passengers on the Titanic

  This data set provides information on the fate of passengers on the
  fatal maiden voyage of the ocean liner ‘Titanic’, summarized according
  to economic status (class), sex, age and survival.

  A 4-dimensional array resulting from cross-tabulating 2201 observations
  on 4 variables. The variables and their levels are as follows:

  +------+------------+-----------------------+
  | No   | Name       | Levels                |
  +------+------------+-----------------------+
  | 1    | Class      | 1st, 2nd, 3rd, Crew   |
  +------+------------+-----------------------+
  | 2    | Sex        | Male, Female          |
  +------+------------+-----------------------+
  | 3    | Age        | Child, Adult          |
  +------+------------+-----------------------+
  | 4    | Survived   | No, Yes               |
  +------+------------+-----------------------+

  Dawson, Robert J. MacG. (1995), The ‘Unusual Episode’ Data Revisited.
  *Journal of Statistics Education*, **3**.
  https://www.amstat.org/publications/jse/v3n3/datasets.dawson.html

  The source provides a data set recording class, sex, age, and survival
  status for each person on board of the Titanic, and is based on data
  originally collected by the British Board of Trade and reprinted in:

  British Board of Trade (1990), *Report on the Loss of the ‘Titanic’
  (S.S.)*. British Board of Trade Inquiry Report (reprint). Gloucester,
  UK: Allan Sutton Publishing.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `titanic.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1313 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'titanic.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/Titanic.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='titanic.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
