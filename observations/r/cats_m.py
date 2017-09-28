# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cats_m(path):
  """Weight Data for Domestic Cats

  The `catsM` data frame has 97 rows and 3 columns.

  144 adult (over 2kg in weight) cats used for experiments with the drug
  digitalis had their heart and body weight recorded. 47 of the cats were
  female and 97 were male. The `catsM` data frame consists of the data
  for the male cats. The full data are in dataset `cats` in package
  `MASS`.

  This data frames contain the following columns:

  `Sex`
      A factor for the sex of the cat (levels are `F` and `M`).

  `Bwt`
      Body weight in kg.

  `Hwt`
      Heart weight in g.

  The data were obtained from

  Fisher, R.A. (1947) The analysis of covariance method for the relation
  between a part and the whole. *Biometrics*, **3**, 65–68.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cats_m.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 97 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cats_m.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/catsM.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cats_m.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
