# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def river_elements(path):
  """RiverElements

  Concentrations of elements in river water samples from upstate NY

  A dataset with 12 observations on the following 27 variables.

  `River`

  One of four rivers: `Grasse`, `Oswegatchie`, `Raquette`, or
  `St. Regis`

  `Site`

  Location: 1=UpStream, 2=MidStream, 3=Downstream

  `Al`

  Aluminum

  `Ba`

  Barium

  `Br`

  Bromine

  `Ca`

  Calcium

  `Ce`

  Cerium

  `Cu`

  Copper

  `Dy`

  Dysprosium

  `Er`

  Erbim

  `Fe`

  Iron

  `Gd`

  Gadolinium

  `Ho`

  Holmum

  `K`

  Potassium

  `La`

  Lathanum

  `Li`

  Lithium

  `Mg`

  Magnesium

  `Mn`

  Manganese

  `Nd`

  Neodymium

  `Pr`

  Proseyodymium

  `Rb`

  Rubidium

  `Si`

  Silicon

  `Sr`

  Strontium

  `Y`

  Yttrium

  `Yb`

  Ytterbium

  `Zn`

  Zinc

  `Zr`

  Zirconium

  Thanks to Dr. Jeff Chiarenzelli of the St. Lawrence University Geology
  Department for the data.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `river_elements.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 27 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'river_elements.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/RiverElements.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='river_elements.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
