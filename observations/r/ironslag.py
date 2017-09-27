# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ironslag(path):
  """Iron Content Measurements

  The `ironslag` data frame has 53 rows and 2 columns. Two methods for
  measuring the iron content in samples of slag were compared, a chemical
  and a magnetic method. The chemical method requires greater effort than
  the magnetic method.

  This data frame contains the following columns:

  chemical
      a numeric vector containing the measurements coming from the
      chemical method

  magnetic
      a numeric vector containing the measurments coming from the magnetic
      method

  Hand, D.J., Daly, F., McConway, K., Lunn, D., and Ostrowski, E. eds
  (1993) A Handbook of Small Data Sets. London: Chapman & Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ironslag.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 53 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ironslag.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/ironslag.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ironslag.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
