# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def slid(path):
  """Survey of Labour and Income Dynamics

  The `SLID` data frame has 7425 rows and 5 columns. The data are from
  the 1994 wave of the Canadian Survey of Labour and Income Dynamics, for
  the province of Ontario. There are missing data, particularly for wages.

  This data frame contains the following columns:

  wages
      Composite hourly wage rate from all jobs.

  education
      Number of years of schooling.

  age
      in years.

  sex
      A factor with levels: `Female`, `Male`.

  language
      A factor with levels: `English`, `French`, `Other`.

  The data are taken from the public-use dataset made available by
  Statistics Canada, and prepared by the Institute for Social Research,
  York University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `slid.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7425 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'slid.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/SLID.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='slid.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
