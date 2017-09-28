# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rotifer(path):
  """Numbers of Rotifers by Fluid Density

  The data give the numbers of rotifers falling out of suspension for
  different fluid densities. There are two species, `pm` *Polyartha
  major* and `kc`, *Keratella cochlearis* and for each species the
  number falling out and the total number are given.

  `density`
      specific density of fluid.

  `pm.y`
      number falling out for *P. major*.

  `pm.total`
      total number of *P. major*.

  `kc.y`
      number falling out for *K. cochlearis*.

  `kc.tot`
      total number of *K. cochlearis*.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rotifer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rotifer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/rotifer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rotifer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
