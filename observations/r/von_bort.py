# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def von_bort(path):
  """Von Bortkiewicz Horse Kicks Data

  Data from von Bortkiewicz (1898), given by Andrews \\& Herzberg (1985),
  on number of deaths by horse or mule kicks in 14 corps of the Prussian
  army.

  A data frame with 280 observations and 4 variables.

  deaths
      number of deaths.

  year
      year of the deaths.

  corps
      factor indicating the corps.

  fisher
      factor indicating whether the corresponding corps was considered by
      Fisher (1925) or not.

  Michael Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/vonbort.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `von_bort.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 280 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'von_bort.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/VonBort.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='von_bort.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
