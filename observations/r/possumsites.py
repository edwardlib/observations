# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def possumsites(path):
  """Possum Sites

  The `possumsites` data frame consists of Longitudes, Latitudes, and
  altitudes for the seven sites from Southern Victoria to central
  Queensland where the `possum` observations were made.

  This data frame contains the following columns:

  Longitude
      a numeric vector

  Latitude
      a numeric vector

  altitude
      in meters

  Lindenmayer, D. B., Viggers, K. L., Cunningham, R. B., and Donnelly, C.
  F. 1995. Morphological variation among columns of the mountain brushtail
  possum, Trichosurus caninus Ogilby (Phalangeridae: Marsupiala).
  Australian Journal of Zoology 43: 449-458.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `possumsites.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'possumsites.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/possumsites.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='possumsites.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
