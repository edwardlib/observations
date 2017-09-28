# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dengue(path):
  """Dengue prevalence, by administrative region

  Data record, for each of 2000 administrative regions, whether or not
  dengue was recorded at any time between 1961 and 1990.

  A data frame with 2000 observations on the following 13 variables.

  humid
      Average vapour density: 1961-1990

  humid90
      90th percentile of `humid`

  temp
      Average temperature: 1961-1990

  temp90
      90th percentile of `temp`

  h10pix
      maximum of `humid`, within a 10 pixel radius

  h10pix90
      maximum of `humid90`, within a 10 pixel radius

  trees
      Percent tree cover, from satellite data

  trees90
      90th percentile of `trees`

  NoYes
      Was dengue observed? (1=yes)

  Xmin
      minimum longitude

  Xmax
      maximum longitude

  Ymin
      minimum latitude

  Ymax
      maximum latitude

  Simon Hales, Environmental Research New Zealand Ltd.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dengue.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2000 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dengue.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/dengue.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dengue.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
