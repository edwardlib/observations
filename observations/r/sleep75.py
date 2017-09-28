# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sleep75(path):
  """sleep75

  Data loads lazily. Type data(sleep75) into the console.

  A data.frame with 706 rows and 34 variables:

  -  age. in years

  -  black. =1 if black

  -  case. identifier

  -  clerical. =1 if clerical worker

  -  construc. =1 if construction worker

  -  educ. years of schooling

  -  earns74. total earnings, 1974

  -  gdhlth. =1 if in good or excel. health

  -  inlf. =1 if in labor force

  -  leis1. sleep - totwrk

  -  leis2. slpnaps - totwrk

  -  leis3. rlxall - totwrk

  -  smsa. =1 if live in smsa

  -  lhrwage. log hourly wage

  -  lothinc. log othinc, unless othinc < 0

  -  male. =1 if male

  -  marr. =1 if married

  -  prot. =1 if Protestant

  -  rlxall. slpnaps + personal activs

  -  selfe. =1 if self employed

  -  sleep. mins sleep at night, per wk

  -  slpnaps. minutes sleep, inc. naps

  -  south. =1 if live in south

  -  spsepay. spousal wage income

  -  spwrk75. =1 if spouse works

  -  totwrk. mins worked per week

  -  union. =1 if belong to union

  -  worknrm. mins work main job

  -  workscnd. mins work second job

  -  exper. age - educ - 6

  -  yngkid. =1 if children < 3 present

  -  yrsmarr. years married

  -  hrwage. hourly wage

  -  agesq. age^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sleep75.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 706 rows and 34 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sleep75.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/sleep75.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sleep75.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
