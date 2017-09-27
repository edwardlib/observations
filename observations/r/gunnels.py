# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gunnels(path):
  """Gunnels

  Presence/absence of gunnels (eels) at shoreline quadrats

  A dataset with 1592 observations on the following 10 variables.

  `Gunnel`

  1= gunnel present in the quadrat or 0=gunnel absent

  `Time`

  Minutes after midnight

  `Fromlow`

  Time in minutes from low tide

  `Slope`

  Slope (to nearest 10 degrees) perpendicular to waterline

  `Rw`

  Percentage cover in quadrat of rockweed/algae/plants

  `Amphiso`

  Density of crustacean food 0=none to 4=high

  `Subst`

  Substratum: 1=solid rock, 2=rocky cobbles, 3=mixed pebbles/sand, 4=fine
  sand,

  5=mud, 6=mixed mud/shell detritus, 7=cobbles on solid rock, 8=cobbles on
  mixed pebbles/sand,

  9=cobbles on fine sand, 10=cobbles on mud, 11=cobbles on mixed mud/shell
  detritus,

  12=cobbles on shell detritus, 13=shell detritus

  `Pool`

  Standing water deep? 1=yes or 2=no

  `Water`

  Standing water in the quadrat? 1=yes or 2=no

  `Cobble`

  Rocky cobbles? 1=yes or 2=no


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gunnels.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1592 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gunnels.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Gunnels.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gunnels.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
