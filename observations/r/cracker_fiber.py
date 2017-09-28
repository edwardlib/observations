# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cracker_fiber(path):
  """Cracker Fiber in Diets

  Digested calories with different types of fiber in crackers

  A dataset with 48 observations on the following 3 variables.

  `Subj`

  ID for the subject

  `Fiber`

  Type of fiber: `bran`, `combo`, `control`, or `gum`

  `Calories`

  Digested calories

  Subset of the data at http://lib.stat.cmu.edu/DASL/Datafiles/Fiber.html,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cracker_fiber.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cracker_fiber.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/CrackerFiber.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cracker_fiber.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
