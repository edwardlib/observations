# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def planets(path):
  """Exoplanets Data

  Data on planets outside the Solar System.

  A data frame with 101 observations from 101 exoplanets on the following
  3 variables.

  mass
      Jupiter mass of the planet.

  period
      period in earth days.

  eccen
      the radial eccentricity of the planet.

  M. Mayor and P. Frei (2003). *New Worlds in the Cosmos: The Discovery of
  Exoplanets*. Cambridge University Press, Cambridge, UK.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `planets.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 101 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'planets.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/planets.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='planets.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
