# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cygob1(path):
  """CYG OB1 Star Cluster Data

  Energy output and surface termperature for Star Cluster CYG OB1.

  A data frame with 47 observations on the following 2 variables.

  `logst`
      log survface termperature of the star.

  `logli`
      log light intensity of the star.

  F. Vanisma and J. P. De Greve (1972), Close binary systems before and
  after mass transfer. *Astrophysics and Space Science*, **87**, 377–401.

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cygob1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 47 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cygob1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/CYGOB1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cygob1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
