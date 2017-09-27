# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ethanol(path):
  """Engine exhaust fumes from burning ethanol

  Ethanol fuel was burned in a single-cylinder engine. For various
  settings of the engine compression and equivalence ratio, the emissions
  of nitrogen oxides were recorded.

  A data frame with 88 observations on the following 3 variables.

  NOx
      Concentration of nitrogen oxides (NO and NO2) in micrograms/J.

  C
      Compression ratio of the engine.

  E
      Equivalence ratio–a measure of the richness of the air and ethanol
      fuel mixture.

  Author(s)
  ~~~~~~~~~

  Documentation contributed by Kevin Wright.

  Brinkman, N.D. (1981) Ethanol Fuel—A Single-Cylinder Engine Study of
  Efficiency and Exhaust Emissions. *SAE transactions*, **90**, 1410–1424.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ethanol.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 88 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ethanol.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lattice/ethanol.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ethanol.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
