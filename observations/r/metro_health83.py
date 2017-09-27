# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def metro_health83(path):
  """MetroHealth83

  Health services data for 83 metropolitan areas

  A dataset with 83 observations on the following 16 variables.

  `City`

  Name of the metropolitan area

  `NumMDs`

  Number of physicians

  `RateMDs`

  Number of physicians per 100,000 people

  `NumHospitals`

  Nmber of community hospitals

  `NumBeds`

  Number of hospital beds

  `RateBeds`

  Number of hospital beds per 100,000 people

  `NumMedicare`

  Number of Medicare recipients in 2003

  `PctChangeMedicare`

  Percent change in Medicare recipients (2000 to 2003)

  `MedicareRate`

  Number of Medicare recipients per 100,000 people

  `SSBNum`

  Number of Social Security recipients in 2004

  `SSBRate`

  Number of Social Security recipients per 100,000 people

  `SSBChange`

  Percent change in Social Security recipients (2000 to 2004)

  `NumRetired`

  Number of retired workers

  `SSINum`

  Number of Supplemental Security Income recipients in 2004

  `SSIRate`

  Number of Supplemental Security Income recipients per 100,000 people

  `SqrtMDs`

  Square root of numver of physicians

  | U.S. Census Bureau: 2006 State and Metropolitan Area Data Book (Table
    B-6)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `metro_health83.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 83 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'metro_health83.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MetroHealth83.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='metro_health83.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
