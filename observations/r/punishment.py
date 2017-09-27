# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def punishment(path):
  """Corporal Punishment Data

  Data from a study of the Gallup Institute in Denmark in 1979 about the
  attitude of a random sample of 1,456 persons towards corporal punishment
  of children.

  A data frame with 36 observations and 5 variables.

  Freq
      frequency.

  attitude
      factor indicating attitude: (no, moderate) punishment of children.

  memory
      factor indicating whether the person had memories of corporal
      punishment as a child (yes, no).

  education
      factor indicating highest level of education (elementary, secondary,
      high).

  age
      factor indicating age group in years (15-24, 25-39, 40-).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  pages 207–208.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `punishment.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'punishment.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Punishment.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='punishment.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
