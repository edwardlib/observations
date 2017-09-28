# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def weightgain(path):
  """Gain in Weight of Rats

  The data arise from an experiment to study the gain in weight of rats
  fed on four different diets, distinguished by amount of protein (low and
  high) and by source of protein (beef and cereal).

  A data frame with 40 observations on the following 3 variables.

  `source`
      source of protein given, a factor with levels `Beef` and
      `Cereal`.

  `type`
      amount of protein given, a factor with levels `High` and `Low`.

  `weightgain`
      weigt gain in grams.

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `weightgain.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'weightgain.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/weightgain.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='weightgain.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
