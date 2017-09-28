# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def president_elections(path):
  """elections for U.S. President, 1932-2012, by state

  Democratic share of the presidential vote, 1932-2012, in each state and
  the District of Columbia.

  -  statecharacter, name of state

  -  demVotenumeric, percent of the vote for president won by the
     Democratic candidate

  -  yearnumeric, integer

  -  southlogical, `TRUE` if state is one of the 11 states of the former
     Confederacy

  David Leip's Atlas of U.S. Presidential Elections
  http://uselectionsatlas.org

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `president_elections.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1047 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'president_elections.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/presidentialElections.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='president_elections.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
