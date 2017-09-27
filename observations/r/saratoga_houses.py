# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def saratoga_houses(path):
  """Houses in Saratoga County (2006)

  Data on houses in Saratoga County, New York, USA in 2006

  A data frame with 1728 observations on the following 16 variables.

  -  `price` price (1000s of US dollars)

  -  `lotSize` size of lot (square feet)

  -  `age` age of house (years)

  -  `landValue` value of land (1000s of US dollars)

  -  `livingArea` living are (square feet)

  -  `pctCollege` percent of neighborhood that graduated college

  -  `bedrooms` number of bedrooms

  -  `firplaces` number of fireplaces

  -  `bathrooms` number of bathrooms (half bathrooms have no shower or
     tub)

  -  `rooms` number of rooms

  -  `heating` type of heating system

  -  `fuel` fuel used for heating

  -  `sewer` type of sewer system

  -  `waterfront` whether property includes waterfront

  -  `newConstruction` whether the property is a new construction

  -  `centralAir` whether the house has central air

  Data collected by Candice Corvetti and used in the "Stat 101" case study
  "How much is a Fireplace Worth". See also

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `saratoga_houses.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1728 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'saratoga_houses.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/SaratogaHouses.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='saratoga_houses.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
