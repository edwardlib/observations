# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def guyer(path):
  """Anonymity and Cooperation

  The `Guyer` data frame has 20 rows and 3 columns. The data are from an
  experiment in which four-person groups played a prisoner's dilemma game
  for 30 trails, each person making either a cooperative or competitive
  choice on each trial. Choices were made either anonymously or in public;
  groups were composed either of females or of males. The observations are
  20 groups.

  This data frame contains the following columns:

  cooperation
      Number of cooperative choices (out of 120 in all).

  condition
      A factor with levels: `A`, Anonymous; `P`, Public-Choice.

  sex
      Sex. A factor with levels: `F`, Female; `M`, Male.

  Fox, J. and Guyer, M. (1978) Public choice and cooperation in n-person
  prisoner's dilemma. *Journal of Conflict Resolution* **22**, 469–481.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `guyer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'guyer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Guyer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='guyer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
