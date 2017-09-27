# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sunspot_year(path):
  """Yearly Sunspot Data, 1700–1988

  Yearly numbers of sunspots from 1700 to 1988 (rounded to one digit).

  Note that monthly numbers are available as `sunspot.month`, though
  starting slightly later.

  The univariate time series `sunspot.year` contains 289 observations,
  and is of class `"ts"`.

  H. Tong (1996) *Non-Linear Time Series*. Clarendon Press, Oxford, p.
  471.

  See Also
  ~~~~~~~~

  For *monthly* sunspot numbers, see `sunspot.month` and `sunspots`.

  Regularly updated yearly sunspot numbers are available from WDC-SILSO,
  Royal Observatory of Belgium, at http://www.sidc.be/silso/datafiles

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sunspot_year.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 289 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sunspot_year.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/sunspot.year.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sunspot_year.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
