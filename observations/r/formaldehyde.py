# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def formaldehyde(path):
  """Determination of Formaldehyde

  These data are from a chemical experiment to prepare a standard curve
  for the determination of formaldehyde by the addition of chromatropic
  acid and concentrated sulphuric acid and the reading of the resulting
  purple color on a spectrophotometer.

  A data frame with 6 observations on 2 variables.

  +--------+----------+-----------+---------------------+
  | [,1]   | carb     | numeric   | Carbohydrate (ml)   |
  +--------+----------+-----------+---------------------+
  | [,2]   | optden   | numeric   | Optical Density     |
  +--------+----------+-----------+---------------------+

  Bennett, N. A. and N. L. Franklin (1954) *Statistical Analysis in
  Chemistry and the Chemical Industry*. New York: Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `formaldehyde.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'formaldehyde.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/Formaldehyde.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='formaldehyde.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
