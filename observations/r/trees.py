# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def trees(path):
  """Girth, Height and Volume for Black Cherry Trees

  This data set provides measurements of the girth, height and volume of
  timber in 31 felled black cherry trees. Note that girth is the diameter
  of the tree (in inches) measured at 4 ft 6 in above the ground.

  A data frame with 31 observations on 3 variables.

  +------------+--------------+-----------+--------------------------------+
  | `[,1]`   | `Girth`    | numeric   | Tree diameter in inches        |
  +------------+--------------+-----------+--------------------------------+
  | `[,2]`   | `Height`   | numeric   | Height in ft                   |
  +------------+--------------+-----------+--------------------------------+
  | `[,3]`   | `Volume`   | numeric   | Volume of timber in cubic ft   |
  +------------+--------------+-----------+--------------------------------+

  Ryan, T. A., Joiner, B. L. and Ryan, B. F. (1976) *The Minitab Student
  Handbook*. Duxbury Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `trees.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 31 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'trees.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/trees.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='trees.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
