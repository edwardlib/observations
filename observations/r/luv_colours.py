# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def luv_colours(path):
  """`colors()` in Luv space

  All built-in `colors()` translated into Luv colour space.

  A data frame with 657 observations and 4 variables:

  L,u,v
      Position in Luv colour space

  col

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `luv_colours.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 657 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'luv_colours.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ggplot2/luv_colours.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='luv_colours.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
