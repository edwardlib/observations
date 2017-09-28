# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def river_iron(path):
  """River Iron

  Amounts of iron in water samples of four rivers

  A dataset with 12 observations on the following 4 variables.

  `River`

  One of four rivers: `Grasse`, `Oswegatchie`, `Raquette`, or
  `St. Regis`

  `Site`

  Location of the site: `DownStream`, `MidStream` or `Upstream`

  `Iron`

  Iron concentration in the water sample (parts per million)

  `LogIron`

  Log (base 10) of iron concentration

  Thanks to Dr. Jeff Chiarenzelli of the St. Lawrence University Geology
  Department for the data.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `river_iron.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'river_iron.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/RiverIron.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='river_iron.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
