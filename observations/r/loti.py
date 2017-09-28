# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def loti(path):
  """Global temperature anomalies

  Anomalies, for the years 1880 to 2010, from the 1951 - 1980 average.
  These are the GISS (Goddard Institute for Space Studies) Land-Ocean
  Temperature Index (LOTI) data

  A data frame with 131 observations on the following 19 variables.

  `Jan`
      a numeric vector

  `Feb`
      a numeric vector

  `Mar`
      a numeric vector

  `Apr`
      a numeric vector

  `May`
      a numeric vector

  `Jun`
      a numeric vector

  `Jul`
      a numeric vector

  `Aug`
      a numeric vector

  `Sep`
      a numeric vector

  `Oct`
      a numeric vector

  `Nov`
      a numeric vector

  `Dec`
      a numeric vector

  `J.D`
      Jan-Dec averages

  `D.N`
      Dec-Nov averages

  `DJF`
      Dec-Jan-Feb averages

  `MAM`
      Mar-Apr-May

  `JJA`
      Jun-Jul-Aug

  `SON`
      Sept-Oct-Nov

  `Year`
      a numeric vector

  http://data.giss.nasa.gov/gistemp/tabledata/GLB.Ts+dSST.txt

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `loti.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 131 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'loti.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gamclass/loti.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='loti.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
