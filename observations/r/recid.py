# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def recid(path):
  """recid

  Data loads lazily. Type data(recid) into the console.

  A data.frame with 1445 rows and 18 variables:

  -  black. =1 if black

  -  alcohol. =1 if alcohol problems

  -  drugs. =1 if drug history

  -  super. =1 if release supervised

  -  married. =1 if married when incarc.

  -  felon. =1 if felony sentence

  -  workprg. =1 if in N.C. pris. work prg.

  -  property. =1 if property crime

  -  person. =1 if crime against person

  -  priors. # prior convictions

  -  educ. years of schooling

  -  rules. # rules violations in prison

  -  age. in months

  -  tserved. time served, rounded to months

  -  follow. length follow period, months

  -  durat. min(time until return, follow)

  -  cens. =1 if duration right censored

  -  ldurat. log(durat)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `recid.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1445 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'recid.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/recid.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='recid.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
