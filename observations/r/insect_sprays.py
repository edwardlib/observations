# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def insect_sprays(path):
  """Effectiveness of Insect Sprays

  The counts of insects in agricultural experimental units treated with
  different insecticides.

  A data frame with 72 observations on 2 variables.

  +--------+---------+-----------+---------------------+
  | [,1]   | count   | numeric   | Insect count        |
  +--------+---------+-----------+---------------------+
  | [,2]   | spray   | factor    | The type of spray   |
  +--------+---------+-----------+---------------------+

  Beall, G., (1942) The Transformation of data from entomological field
  experiments, *Biometrika*, **29**, 243–262.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `insect_sprays.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'insect_sprays.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/InsectSprays.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='insect_sprays.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
