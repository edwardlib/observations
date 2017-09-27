# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def summer(path):
  """Air pollution data, separately for summer and winter months

  Air pollution data from Leeds (U.K.) city centre, collected from 1994 to
  1998. The `summer` data set corresponds to the months of April to July
  inclusive. The `winter` data set corresponds to the months of November
  to February inclusive. Some outliers have been removed, as discussed by
  Heffernan and Tawn, 2004.

  Data frames with 578 (summer) and 532 (winter) observations on the
  following 5 variables.

  O3
      Daily maximum ozone in parts per billion.

  NO2
      Daily maximum NO2 in parts per billion.

  NO
      Daily maximum NO in parts per billion.

  SO2
      Daily maximum SO2 in parts per billion.

  PM10
      Daily maximum PM10 in micrograms/metre^3

  Provided as online supplementary material to Heffernan and Tawn, 2004:

  http://www.blackwellpublishing.com/rss/Readmefiles/heffernan.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `summer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 578 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'summer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/texmex/summer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='summer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
