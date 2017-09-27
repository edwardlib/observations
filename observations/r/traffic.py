# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def traffic(path):
  """Effect of Swedish Speed Limits on Accidents

  An experiment was performed in Sweden in 1961–2 to assess the effect of
  a speed limit on the motorway accident rate. The experiment was
  conducted on 92 days in each year, matched so that day `j` in 1962 was
  comparable to day `j` in 1961. On some days the speed limit was in
  effect and enforced, while on other days there was no speed limit and
  cars tended to be driven faster. The speed limit days tended to be in
  contiguous blocks.

  This data frame contains the following columns:

  `year`
      1961 or 1962.

  `day`
      of year.

  `limit`
      was there a speed limit?

  `y`
      traffic accident count for that day.

  Svensson, A. (1981) On the goodness-of-fit test for the multiplicative
  Poisson model. *Annals of Statistics,* **9**, 697–704.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `traffic.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 184 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'traffic.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Traffic.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='traffic.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
