# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def forbes2000(path):
  """The Forbes 2000 Ranking of the World's Biggest Companies (Year 2004)

  The Forbes 2000 list is a ranking of the world's biggest companies,
  measured by sales, profits, assets and market value.

  A data frame with 2000 observations on the following 8 variables.

  rank
      the ranking of the company.

  name
      the name of the company.

  country
      a factor giving the country the company is situated in.

  category
      a factor describing the products the company produces.

  sales
      the amount of sales of the company in billion USD.

  profits
      the profit of the company in billion USD.

  assets
      the assets of the company in billion USD.

  marketvalue
      the market value of the company in billion USD.

  http://www.forbes.com, assessed on November 26th, 2004.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `forbes2000.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2000 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'forbes2000.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/Forbes2000.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='forbes2000.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
