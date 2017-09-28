# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def athlet2(path):
  """athlet2

  Data loads lazily. Type data(athlet2) into the console.

  A data.frame with 30 rows and 10 variables:

  -  dscore. home scr. - vist. scr., 1993

  -  dinstt. diff. in-state tuit., 1994

  -  doutstt. diff. out-state tuit., 1994

  -  htpriv. =1 if home team priv. sch.

  -  vtpriv. =1 if vist. team priv. sch.

  -  dapps. diff. in applications, 1994

  -  htwrd. =1 if home win. record, 1993

  -  vtwrd. =1 if vist. win. record, 1993

  -  dwinrec. htwrd - vtwrd

  -  dpriv. htpriv - vtpriv

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `athlet2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'athlet2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/athlet2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='athlet2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
