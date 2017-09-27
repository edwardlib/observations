# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def frostedflakes(path):
  """Frosted Flakes data

  The `frosted flakes` data frame has 101 rows and 2 columns giving the
  sugar concentration (in percent) for 25 g samples of a cereal as
  measured by 2 methods – high performance liquid chromatography (a slow
  accurate lab method) and a quick method using the infra-analyzer 400.

  This data frame contains the following columns:

  Lab
      careful laboratory analysis measurements using high performance
      liquid chromatography

  IA400
      measurements based on the infra-analyzer 400


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `frostedflakes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'frostedflakes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/frostedflakes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='frostedflakes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
