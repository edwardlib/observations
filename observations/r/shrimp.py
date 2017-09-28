# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def shrimp(path):
  """Percentage of Shrimp in Shrimp Cocktail

  A numeric vector with 18 determinations by different laboratories of the
  amount (percentage of the declared total weight) of shrimp in shrimp
  cocktail.

  F. J. King and J. J. Ryan (1976) Collaborative study of the
  determination of the amount of shrimp in shrimp cocktail. *J. Off. Anal.
  Chem.* **59**, 644–649.

  R. G. Staudte and S. J. Sheather (1990) *Robust Estimation and Testing.*

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `shrimp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'shrimp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/shrimp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='shrimp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
