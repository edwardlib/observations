# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pollster08(path):
  """Pollster08

  Polls for 2008 U.S. presidential election

  A dataset with 102 observations on the following 11 variables.

  `PollTaker`

  Polling organization

  `PollDates`

  Dates the poll data were collected

  `MidDate`

  Midpoint of the polling period

  `Days`

  Number of days after August 28th (end of Democratic convention)

  `n`

  Sample size for the poll

  `Pop`

  `A`\ =all, `LV`\ =likely voters, `RV`\ =registered voters

  `McCain`

  Percent supporting John McCain

  `Obama`

  Percent supporting Barak Obama

  `Margin`

  Obama percent minus McCain percent

  `Charlie`

  Indicator for polls after Charlie Gibson interview with VP candidate
  Sarah Palin (9/11)

  `Meltdown`

  Indicator for polls after Lehman Brothers bankruptcy (9/15)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pollster08.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 102 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pollster08.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Pollster08.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pollster08.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
