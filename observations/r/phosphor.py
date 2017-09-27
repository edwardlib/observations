# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def phosphor(path):
  """Phosphorus Content Data

  This dataset investigates the effect from inorganic and organic
  Phosphorus in the soil upon the phosphorus content of the corn grown in
  this soil, from Prescott (1975).

  A data frame with 18 observations on the following 3 variables.

  `inorg`
      Inorganic soil Phosphorus

  `organic`
      Organic soil Phosphorus

  `plant`
      Plant Phosphorus content

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection.* Wiley, p.156, table 24.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `phosphor.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'phosphor.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/phosphor.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='phosphor.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
