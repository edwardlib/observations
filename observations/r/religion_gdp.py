# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def religion_gdp(path):
  """ReligionGDP

  Data on religiosity of countries from the Pew Global Attitudes Project

  A dataset with 44 observations on the following 9 variables.

  `Country`

  Name of country

  `Religiosity`

  A measure of degree of religiosity for residents of the country

  `GDP`

  Per capita Gross Domestic Product in the country

  `Africa`

  Indicator for countries in Africa

  `EastEurope`

  Indicator for countries in Eastern Europe

  `MiddleEast`

  Indicator for countries in the Middle East

  `Asia`

  Indicator for countries in Asia

  `WestEurope`

  Indicator for countries in Western Europe

  `Americas`

  Indicator for countries in North/South America

  Data from the 2007 Spring Survey conducted through the Pew Global

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `religion_gdp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 44 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'religion_gdp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/ReligionGDP.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='religion_gdp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
