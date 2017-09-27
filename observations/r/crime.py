# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crime(path):
  """Crime in North Carolina

  a panel of 90 observations from 1981 to 1987

  *number of observations* : 630

  *observation* : regional

  *country* : United States

  A dataframe containing :

  county
      county identifier

  year
      year from 1981 to 1987

  crmrte
      crimes committed per person

  prbarr
      'probability' of arrest

  prbconv
      'probability' of conviction

  prbpris
      'probability' of prison sentence

  avgsen
      average sentence, days

  polpc
      police per capita

  density
      people per square mile

  taxpc
      tax revenue per capita

  region
      one of 'other', 'west' or 'central'

  smsa
      'yes' or 'no' if in SMSA

  pctmin
      percentage minority in 1980

  wcon
      weekly wage in construction

  wtuc
      weekly wage in trns, util, commun

  wtrd
      weekly wage in whole sales and retail trade

  wfir
      weekly wage in finance, insurance and real estate

  wser
      weekly wage in service industry

  wmfg
      weekly wage in manufacturing

  wfed
      weekly wage of federal employees

  wsta
      weekly wage of state employees

  wloc
      weekly wage of local governments employees

  mix
      offence mix: face-to-face/other

  pctymle
      percentage of young males

  Cornwell, C. and W.N. Trumbull (1994) “Estimating the economic model of
  crime with panel data”, *Review of Economics and Statistics*, **76**,
  360–366.

  Baltagi, B. H. (forthcoming) “Estimating an economic model of crime
  using panel data from North Carolina”, *Journal of Applied
  Econometrics*, .

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crime.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 630 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crime.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Crime.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crime.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
