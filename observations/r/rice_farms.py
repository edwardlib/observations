# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rice_farms(path):
  """Production of Rice in India

  a panel of 171 observations

  *number of observations* : 1026

  *observation* : farms

  *country* : Indonesia

  A dataframe containing :

  id
      the farm identifier

  size
      the total area cultivated with rice, measured in hectares

  status
      land status, on of `'owner'` (non sharecroppers, owner operators
      or leaseholders or both), `'share'` (sharecroppers), `'mixed'`
      (mixed of the two previous status)

  varieties
      one of `'trad'` (traditional varieties), `'high'` (high yielding
      varieties) and `'mixed'` (mixed varieties)

  bimas
      bIMAS is an intensification program; one of `'no'` (non-bimas
      farmer), `'yes'` (bimas farmer) or `'mixed'` (part but not all
      of farmer's land was registered to be in the bimas program)

  seed
      seed in kilogram

  urea
      urea in kilogram

  phosphate
      phosphate in kilogram

  pesticide
      pesticide cost in Rupiah

  pseed
      price of seed in Rupiah per kg

  purea
      price of urea in Rupiah per kg

  pphosph
      price of phosphate in Rupiah per kg

  hiredlabor
      hired labor in hours

  famlabor
      family labor in hours

  totlabor
      total labor (excluding harvest labor)

  wage
      labor wage in Rupiah per hour

  goutput
      gross output of rice in kg

  noutput
      net output, gross output minus harvesting cost (paid in terms of
      rice)

  price
      price of rough rice in Rupiah per kg

  region
      one of `'wargabinangun'`, `'langan'`, `'gunungwangi'`,
      `'malausma'`, `'sukaambit'`, `'ciwangi'`

  Qu Feng and William C. Horrace, (2012) “Alternative Measures of
  Technical Efficiency: Skew, Bias and Scale”, *Journal of Applied

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rice_farms.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1026 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rice_farms.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/RiceFarms.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rice_farms.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
