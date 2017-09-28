# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def agriculture(path):
  """European Union Agricultural Workforces

  Gross National Product (GNP) per capita and percentage of the population
  working in agriculture for each country belonging to the European Union
  in 1993.

  A data frame with 12 observations on 2 variables:

  +----------+---------+-----------+-----------------------------+
  | [ , 1]   | `x`   | numeric   | per capita GNP              |
  +----------+---------+-----------+-----------------------------+
  | [ , 2]   | `y`   | numeric   | percentage in agriculture   |
  +----------+---------+-----------+-----------------------------+

  The row names of the data frame indicate the countries.

  Eurostat (European Statistical Agency, 1994): *Cijfers en feiten: Een
  statistisch portret van de Europese Unie*.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `agriculture.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'agriculture.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/agriculture.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='agriculture.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
