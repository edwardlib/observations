# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def minard_cities(path):
  """Data from Minard's famous graphic map of Napoleon's march on Moscow

  Charles Joseph Minard's graphic depiction of the fate of Napoleon's
  Grand Army in the Russian campaign of 1815 has been called the "greatest
  statistical graphic ever drawn" (Tufte, 1983). Friendly (2002) describes
  some background for this graphic, and presented it as Minard's Chalenge:
  to reproduce it using modern statistical or graphic software, in a way
  that showed the elegance of some computer language to both describe and
  produce this graphic.

  `Minard.troops`: A data frame with 51 observations on the following 5
  variables giving the number of surviving troops.

  `long`
      Longitude

  `lat`
      Latitude

  `survivors`
      Number of surviving troops, a numeric vector

  `direction`
      a factor with levels `A` ("Advance") `R` ("Retreat")

  `group`
      a numeric vector

  `Minard.cities`: A data frame with 20 observations on the following 3
  variables giving the locations of various places along the path of
  Napoleon's army.

  `long`
      Longitude

  `lat`
      Latitude

  `city`
      City name: a factor with levels `Bobr` `Chjat` ... `Witebsk`
      `Wixma`

  `Minard.temp`: A data frame with 9 observations on the following 4
  variables, giving the temperature at various places along the march of
  retreat from Moscow.

  `long`
      Longitude

  `temp`
      Temperature

  `days`
      Number of days on the retreat march

  `date`
      a factor with levels `Dec01` `Dec06` `Dec07` `Nov09`
      `Nov14` `Nov28` `Oct18` `Oct24`

  http://www.cs.uic.edu/~wilkinson/TheGrammarOfGraphics/minard.txt

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `minard_cities.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'minard_cities.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Minard.cities.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='minard_cities.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
