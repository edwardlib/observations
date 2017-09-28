# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def menarche(path):
  """Age of Menarche in Warsaw

  Proportions of female children at various ages during adolescence who
  have reached menarche.

  This data frame contains the following columns:

  `Age`
      Average age of the group. (The groups are reasonably age
      homogeneous.)

  `Total`
      Total number of children in the group.

  `Menarche`
      Number who have reached menarche.

  Milicer, H. and Szczotka, F. (1966) Age at Menarche in Warsaw girls in
  1965. *Human Biology* **38**, 199–203.

  | The data are also given in
  | Aranda-Ordaz, F.J. (1981) On two families of transformations to
    additivity for binary response data. *Biometrika* **68**, 357–363.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `menarche.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'menarche.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/menarche.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='menarche.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
