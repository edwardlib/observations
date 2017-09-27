# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hotspots(path):
  """Hawaian island chain hotspot Potassium-Argon ages

  K-Ar Ages (millions of years) and distances (km) from Kilauea along the
  trend of the chain of Hawaian volcanic islands and other seamounts that
  are believed to have been created by a moving "hot spot". The age of
  Kilauea is given as 0-0.4 Ma.

  A data frame with 36 observations on the following 6 variables.

  `ID`
      Volcano identifier

  `name`
      Name

  `distance`
      Distance in kilometers

  `age`
      K-Ar age in millions of years

  `error`
      Standard error of estimate?

  `source`
      Data source; see information on web site below.

  http://www.soest.hawaii.edu/GG/HCV/haw_formation.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hotspots.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 35 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hotspots.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/hotspots.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hotspots.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
