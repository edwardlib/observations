# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def species_area(path):
  """Species Area

  Land area and number of mammal species for island in Southeast Asia

  A dataset with 14 observations on the following 5 variables.

  `Name`

  Name of the island

  `Area`

  Area (in sq. km)

  `Species`

  Number of mammal species

  `logArea`

  Natural logarithm (base e) of Area

  `logSpecies`

  Natural logarithm (base e) of Species

  Heaney, Lawrence R. (1984) Mammalian species richness on islands on the

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `species_area.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'species_area.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/SpeciesArea.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='species_area.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
