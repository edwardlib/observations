# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cities1(path):
  """Distances between 11 US cities

  Airline distances between 11 US cities may be used as an example for
  multidimensional scaling or cluster analysis.

  A data frame with 11 observations on the following 11 variables.

  `ATL`
      Atlana, Georgia

  `BOS`
      Boston, Massachusetts

  `ORD`
      Chicago, Illinois

  `DCA`
      Washington, District of Columbia

  `DEN`
      Denver, Colorado

  `LAX`
      Los Angeles, California

  `MIA`
      Miami, Florida

  `JFK`
      New York, New York

  `SEA`
      Seattle, Washington

  `SFO`
      San Francisco, California

  `MSY`
      New Orleans, Lousianna

  http://www.timeanddate.com/worldclock/distance.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cities1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cities1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/cities.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cities1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
