# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mammals(path):
  """Brain and Body Weights for 62 Species of Land Mammals

  A data frame with average brain and body weights for 62 species of land
  mammals.

  `body`
      body weight in kg.

  `brain`
      brain weight in g.

  `name`
      Common name of species. (Rock hyrax-a = *Heterohyrax brucci*, Rock
      hyrax-b = *Procavia habessinic.*.)

  Weisberg, S. (1985) *Applied Linear Regression.* 2nd edition. Wiley, pp.
  144–5.

  Selected from: Allison, T. and Cicchetti, D. V. (1976) Sleep in mammals:
  ecological and constitutional correlates. *Science* **194**, 732–734.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mammals.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mammals.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/mammals.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mammals.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
