# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cats(path):
  """Anatomical Data from Domestic Cats

  The heart and body weights of samples of male and female cats used for
  *digitalis* experiments. The cats were all adult, over 2 kg body weight.

  This data frame contains the following columns:

  `Sex`
      sex: Factor with evels `"F"` and `"M"`.

  `Bwt`
      body weight in kg.

  `Hwt`
      heart weight in g.

  R. A. Fisher (1947) The analysis of covariance method for the relation
  between a part and the whole, *Biometrics* **3**, 65–68.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cats.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 144 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cats.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/cats.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cats.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
