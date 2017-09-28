# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nerlove(path):
  """Cost Function for Electricity Producers, 1955

  a cross-section from 1955 to 1955

  *number of observations* : 159

  *observation* : production units

  *country* : United States

  A dataframe containing :

  cost
      total cost

  output
      total output

  pl
      wage rate

  sl
      cost share for labor

  pk
      capital price index

  sk
      cost share for capital

  pf
      fuel price

  sf
      cost share for fuel

  Nerlove, M. (1963) *Returns to scale in electricity industry* *in*
  Christ, C. ed. (1963) *Measurement in Economics: Studies in Mathematical
  Economics and Econometrics in Memory of Yehuda Grunfeld* , Stanford,
  California, Stanford University Press .

  Christensen, L. and W. H. Greene (1976) “Economies of scale in U.S.
  electric power generation”, *Journal of Political Economy*, **84**,
  655-676.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nerlove.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 159 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nerlove.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Nerlove.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nerlove.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
