# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hc_choice_california(path):
  """Heating and Cooling System Choice in Newly Built Houses in California

  a cross-section

  *number of observations* : 250

  *observation* : households

  *country* : California

  A dataframe containing :

  depvar
      heating system, one of gcc (gas central heat with cooling), ecc
      (electric central resistence heat with cooling), erc (electric room
      resistence heat with cooling), hpc (electric heat pump which
      provides cooling also), gc (gas central heat without cooling, ec
      (electric central resistence heat without cooling), er (electric
      room resistence heat without cooling)

  ich.z
      installation cost of the heating portion of the system

  icca
      installation cost for cooling

  och.z
      operating cost for the heating portion of the system

  occa
      operating cost for cooling

  income
      annual income of the household

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hc_choice_california.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 250 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hc_choice_california.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/HC.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hc_choice_california.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
