# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def quakes(path):
  """Locations of Earthquakes off Fiji

  The data set give the locations of 1000 seismic events of MB > 4.0. The
  events occurred in a cube near Fiji since 1964.

  A data frame with 1000 observations on 5 variables.

  +--------+------------+-----------+--------------------------------+
  | [,1]   | lat        | numeric   | Latitude of event              |
  +--------+------------+-----------+--------------------------------+
  | [,2]   | long       | numeric   | Longitude                      |
  +--------+------------+-----------+--------------------------------+
  | [,3]   | depth      | numeric   | Depth (km)                     |
  +--------+------------+-----------+--------------------------------+
  | [,4]   | mag        | numeric   | Richter Magnitude              |
  +--------+------------+-----------+--------------------------------+
  | [,5]   | stations   | numeric   | Number of stations reporting   |
  +--------+------------+-----------+--------------------------------+

  This is one of the Harvard PRIM-H project data sets. They in turn
  obtained it from Dr. John Woodhouse, Dept. of Geophysics, Harvard
  University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `quakes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1000 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'quakes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/quakes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='quakes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
