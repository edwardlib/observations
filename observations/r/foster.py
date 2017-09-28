# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def foster(path):
  """Foster Feeding Experiment

  The data are from a foster feeding experiment with rat mothers and
  litters of four different genotypes. The measurement is the litter
  weight after a trial feeding period.

  A data frame with 61 observations on the following 3 variables.

  `litgen`
      genotype of the litter, a factor with levels `A`, `B`, `I`,
      and `J`.

  `motgen`
      genotype of the mother, a factor with levels `A`, `B`, `I`,
      and `J`.

  `weight`
      the weight of the litter after a feeding period.

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `foster.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 61 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'foster.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/foster.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='foster.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
