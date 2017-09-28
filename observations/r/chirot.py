# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chirot(path):
  """The 1907 Romanian Peasant Rebellion

  The `Chirot` data frame has 32 rows and 5 columns. The observations
  are counties in Romania.

  This data frame contains the following columns:

  intensity
      Intensity of the rebellion

  commerce
      Commercialization of agriculture

  tradition
      Traditionalism

  midpeasant
      Strength of middle peasantry

  inequality
      Inequality of land tenure

  Chirot, D. and C. Ragin (1975) The market, tradition and peasant
  rebellion: The case of Romania. *American Sociological Review* **40**,
  428–444 [Table 1].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chirot.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chirot.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Chirot.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chirot.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
