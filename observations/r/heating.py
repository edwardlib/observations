# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def heating(path):
  """Heating System Choice in California Houses

  a cross-section

  *number of observations* : 900

  *observation* : households

  *country* : California

  A dataframe containing :

  idcase
      id

  depvar
      heating system, one of gc (gas central), gr (gas room), ec (electric
      central), er (electric room), hp (heat pump)

  ic.z
      installation cost for heating system z (defined for the 5 heating
      systems)

  oc.z
      annual operating cost for heating system z (defined for the 5
      heating systems)

  pb.z
      ratio oc.z/ic.z

  income
      annual income of the household

  agehed
      age of the household head

  rooms
      numbers of rooms in the house

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `heating.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 900 rows and 21 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'heating.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Heating.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='heating.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
