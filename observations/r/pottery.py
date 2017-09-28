# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pottery(path):
  """Chemical Composition of Pottery

  The data give the chemical composition of ancient pottery found at four
  sites in Great Britain. They appear in Hand, et al. (1994), and are used
  to illustrate MANOVA in the SAS Manual. (Suggested by Michael Friendly.)

  A data frame with 26 observations on the following 6 variables.

  `Site`
      a factor with levels `AshleyRails` `Caldicot` `IsleThorns`
      `Llanedyrn`

  `Al`
      Aluminum

  `Fe`
      Iron

  `Mg`
      Magnesium

  `Ca`
      Calcium

  `Na`
      Sodium

  Hand, D. J., Daly, F., Lunn, A. D., McConway, K. J., and E., O. (1994)
  *A Handbook of Small Data Sets*. Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pottery.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pottery.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Pottery.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pottery.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
