# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def injury(path):
  """injury

  Data loads lazily. Type data(injury) into the console.

  A data.frame with 7150 rows and 30 variables:

  -  durat. duration of benefits

  -  afchnge. =1 if after change in benefits

  -  highearn. =1 if high earner

  -  male. =1 if male

  -  married. =1 if married

  -  hosp. =1 if inj. required hosp. stay

  -  indust. industry

  -  injtype. type of injury

  -  age. age at time of injury

  -  prewage. previous weekly wage, 1982 $

  -  totmed. total med. costs, 1982 $

  -  injdes. 4 digit injury description

  -  benefit. real dollar value of benefit

  -  ky. =1 for kentucky

  -  mi. =1 for michigan

  -  ldurat. log(durat)

  -  afhigh. afchnge\*highearn

  -  lprewage. log(wage)

  -  lage. log(age)

  -  ltotmed. log(totmed); = 0 if totmed < 1

  -  head. =1 if head injury

  -  neck. =1 if neck injury

  -  upextr. =1 if upper extremities injury

  -  trunk. =1 if trunk injury

  -  lowback. =1 if lower back injury

  -  lowextr. =1 if lower extremities injury

  -  occdis. =1 if occupational disease

  -  manuf. =1 if manufacturing industry

  -  construc. =1 if construction industry

  -  highlpre. highearn\*lprewage

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `injury.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7150 rows and 30 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'injury.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/injury.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='injury.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
