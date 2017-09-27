# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def film(path):
  """Film

  Film data from Maltin's Movie and Video Guide

  A dataset with 100 observations on the following 9 variables.

  `Title`

  Movie title

  `Year`

  Year the movie was released

  `Time`

  Running time (in minutes)

  `Cast`

  Number of cast members listed in the guide

  `Rating`

  Maltin rating (range is 1 to 4, in steps of 0.5)

  `Description`

  Number of lines of text Maltin uses to describe the movie

  `Origin`

  Country: 0 = USA, 1 = Great Britain, 2 = France, 3 = Italy, 4 = Canada

  `Time_code`

  `long`\ =90 minues or longer `short`\ =under 90 minutes

  `Good`

  `1`\ =rating or 3 stars or better `0`\ =any lower rating


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `film.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'film.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Film.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='film.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
