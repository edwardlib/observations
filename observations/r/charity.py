# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def charity(path):
  """charity

  Data loads lazily. Type data(charity) into the console.

  A data.frame with 4268 rows and 8 variables:

  -  respond. =1 if responded with gift

  -  gift. amount of gift, Dutch guilders

  -  resplast. =1 if responded to most recent mailing

  -  weekslast. number of weeks since last response

  -  propresp. response rate to mailings

  -  mailsyear. number of mailings per year

  -  giftlast. amount of most recent gift

  -  avggift. average of past gifts

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `charity.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4268 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'charity.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/charity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='charity.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
