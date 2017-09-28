# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def youth_risk2009(path):
  """YouthRisk2009

  Survey of students in grades 9-12 concerning health-risk behiviors

  A dataset with 500 observations on the following 6 variables.

  `Sleep`

  Average hours sleep on school night, coded with `10 or more hours`,
  `9 hours`,

  ]tab `8 hours`, `7 hours`, `6 hours`, `5 hours`, or
  `4 or less hours`

  `Sleep7`

  Seven or more hours of sleep? 0=\ `No`, 1=\ `Yes`

  `SmokeLife`

  Ever smoked? `No` or `Yes`

  `SmokeDaily`

  Regular smoker? `No` or `Yes`

  `MarijuaEver`

  Ever smoked marijuana? 0=\ `No` or 1=\ `Yes`

  `Age`

  Age (in years)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `youth_risk2009.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 500 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'youth_risk2009.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/YouthRisk2009.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='youth_risk2009.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
