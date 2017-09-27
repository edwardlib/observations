# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def alcohol(path):
  """Alcohol Solubility in Water Data

  The solubility of alcohols in water is important in understanding
  alcohol transport in living organisms. This dataset from (Romanelli et
  al., 2001) contains physicochemical characteristics of 44 aliphatic
  alcohols. The aim of the experiment was the prediction of the solubility
  on the basis of molecular descriptors.

  A data frame with 44 observations on the following 7 numeric variables.

  `SAG`
      solvent accessible surface-bounded molecular volume.

  `V`
      volume

  `logPC`
      Log(PC); PC = octanol-water partitions coefficient

  `P`
      polarizability

  `RM`
      molar refractivity

  `Mass`
      the mass

  `logSolubility`
      ln(Solubility), the response.

  The website accompanying the MMY-book:
  http://www.wiley.com/legacy/wileychi/robust_statistics

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `alcohol.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9822 rows and 33 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'alcohol.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/alcohol.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='alcohol.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
