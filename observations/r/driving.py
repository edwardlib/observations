# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def driving(path):
  """driving

  Data loads lazily. Type data(driving) into the console.

  A data.frame with 1200 rows and 56 variables:

  -  year. 1980 through 2004

  -  state. 48 continental states, alphabetical

  -  sl55. speed limit == 55

  -  sl65. speed limit == 65

  -  sl70. speed limit == 70

  -  sl75. speed limit == 75

  -  slnone. no speed limit

  -  seatbelt. =0 if none, =1 if primary, =2 if secondary

  -  minage. minimum drinking age

  -  zerotol. zero tolerance law

  -  gdl. graduated drivers license law

  -  bac10. blood alcohol limit .10

  -  bac08. blood alcohol limit .08

  -  perse. administrative license revocation (per se law)

  -  totfat. total traffic fatalities

  -  nghtfat. total nighttime fatalities

  -  wkndfat. total weekend fatalities

  -  totfatpvm. total fatalities per 100 million miles

  -  nghtfatpvm. nighttime fatalities per 100 million miles

  -  wkndfatpvm. weekend fatalities per 100 million miles

  -  statepop. state population

  -  totfatrte. total fatalities per 100,000 population

  -  nghtfatrte. nighttime fatalities per 100,000 population

  -  wkndfatrte. weekend accidents per 100,000 population

  -  vehicmiles. vehicle miles traveled, billions

  -  unem. unemployment rate, percent

  -  perc14\_24. percent population aged 14 through 24

  -  sl70plus. sl70 + sl75 + slnone

  -  sbprim. =1 if primary seatbelt law

  -  sbsecon. =1 if secondary seatbelt law

  -  d80. =1 if year == 1980

  -  d81.

  -  d82.

  -  d83.

  -  d84.

  -  d85.

  -  d86.

  -  d87.

  -  d88.

  -  d89.

  -  d90.

  -  d91.

  -  d92.

  -  d93.

  -  d94.

  -  d95.

  -  d96.

  -  d97.

  -  d98.

  -  d99.

  -  d00.

  -  d01.

  -  d02.

  -  d03.

  -  d04. =1 if year == 2004

  -  vehicmilespc.

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `driving.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1200 rows and 56 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'driving.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/driving.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='driving.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
