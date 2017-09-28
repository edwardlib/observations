# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def schmid(path):
  """12 variables created by Schmid and Leiman to show the Schmid-Leiman Transf
  ormation

  John Schmid and John M. Leiman (1957) discuss how to transform a
  hierarchical factor structure to a bifactor structure. Schmid contains
  the example 12 x 12 correlation matrix. schmid.leiman is a 12 x 12
  correlation matrix with communalities on the diagonal. This can be used
  to show the effect of correcting for attenuation. Two additional data
  sets are taken from Chen et al. (2006).

  John Schmid Jr. and John. M. Leiman (1957), The development of
  hierarchical factor solutions.Psychometrika, 22, 83-90.

  F.F. Chen, S.G. West, and K.H. Sousa.(2006) A comparison of bifactor and
  second-order models of quality of life. Multivariate Behavioral
  Research, 41(2):189-225, 2006.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `schmid.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'schmid.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Schmid.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='schmid.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
