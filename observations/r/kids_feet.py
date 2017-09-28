# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kids_feet(path):
  """Foot measurements in children

  These data were collected by a statistician, Mary C. Meyer, in a fourth
  grade classroom in Ann Arbor, MI, in October 1997. They are a
  convenience sample — the kids who were in the fourth grade.

  A data frame with 39 observations on the following variables.

  -  `name` a factor with levels corresponding to the name of each child

  -  `birthmonth` the month of birth

  -  `birthyear` the year of birth

  -  `length` length of longer foot (in cm)

  -  `width` width of longer foot (in cm)

  -  `sex` a factor with levels `B` `G`

  -  `biggerfoot` a factor with levels `L` `R`

  -  `domhand` a factor with levels `L` `R`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kids_feet.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 39 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kids_feet.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/KidsFeet.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kids_feet.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
