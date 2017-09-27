# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def attend(path):
  """attend

  Data loads lazily. Type data(attend) into the console.

  A data.frame with 680 rows and 11 variables:

  -  attend. classes attended out of 32

  -  termGPA. GPA for term

  -  priGPA. cumulative GPA prior to term

  -  ACT. ACT score

  -  final. final exam score

  -  atndrte. percent classes attended

  -  hwrte. percent homework turned in

  -  frosh. =1 if freshman

  -  soph. =1 if sophomore

  -  missed. number of classes missed

  -  stndfnl. (final - mean)/sd

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `attend.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 680 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'attend.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/attend.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='attend.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
