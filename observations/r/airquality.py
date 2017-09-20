from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def airquality(path):
  """New York Air Quality Measurements

  Daily air quality measurements in New York, May to September 1973.

  A data frame with 154 observations on 6 variables.

  +------------+---------------+-----------+---------------------------+
  | `[,1]`   | `Ozone`     | numeric   | Ozone (ppb)               |
  +------------+---------------+-----------+---------------------------+
  | `[,2]`   | `Solar.R`   | numeric   | Solar R (lang)            |
  +------------+---------------+-----------+---------------------------+
  | `[,3]`   | `Wind`      | numeric   | Wind (mph)                |
  +------------+---------------+-----------+---------------------------+
  | `[,4]`   | `Temp`      | numeric   | Temperature (degrees F)   |
  +------------+---------------+-----------+---------------------------+
  | `[,5]`   | `Month`     | numeric   | Month (1--12)             |
  +------------+---------------+-----------+---------------------------+
  | `[,6]`   | `Day`       | numeric   | Day of month (1--31)      |
  +------------+---------------+-----------+---------------------------+

  The data were obtained from the New York State Department of
  Conservation (ozone data) and the National Weather Service
  (meteorological data).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `airquality.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 153 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'airquality.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/datasets/airquality.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='airquality.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
