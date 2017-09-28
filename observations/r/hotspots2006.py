# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hotspots2006(path):
  """Hawaian island chain hotspot Argon-Argon ages

  Ar-Ar Ages (millions of years) and distances (km) from Kilauea along the
  trend of the chain of Hawaian volcanic islands and other seamounts that
  are believed to have been created by a moving "hot spot".

  A data frame with 10 observations on the following 6 variables.

  `age`
      Ar-Ar age

  `CI95lim`
      Measurement error; 95% CI

  `geoErr`
      Geological Uncertainty

  `totplus`
      Total uncertainty (+)

  `totminus`
      Total uncertainty (-)

  `distance`
      Distance in kilometers

  Warren D. Sharp and David A. Clague, 50-Ma initiation of
  Hawaiian-Emperor bend records major change in Pacific Plate motion.
  Science 313: 1281-1284 (2006).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hotspots2006.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hotspots2006.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/hotspots2006.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hotspots2006.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
