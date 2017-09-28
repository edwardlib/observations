# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fossilfuel(path):
  """Fossil Fuel Data

  Estimates of total worldwide carbon emissions from fossil fuel use.

  This data frame contains the following columns:

  year
      a numeric vector giving the year the measurement was taken.

  carbon
      a numeric vector giving the total worldwide carbon emissions from
      fossil fuel use, in millions of tonnes.

  Marland et al (2003)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fossilfuel.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fossilfuel.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/fossilfuel.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fossilfuel.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
