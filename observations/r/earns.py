# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def earns(path):
  """earns

  Data loads lazily. Type data(earns) into the console.

  A data.frame with 41 rows and 14 variables:

  -  year. 1947 to 1987

  -  wkearns. avg. real weekly earnings

  -  wkhours. avg. weekly hours

  -  outphr. output per labor hour

  -  hrwage. wkearns/wkhours

  -  lhrwage. log(hrwage)

  -  loutphr. log(outphr)

  -  t. time trend: t=1 to 47

  -  ghrwage. lhrwage - lhrwage[\_n-1]

  -  goutphr. loutphr - loutphr[\_n-1]

  -  ghrwge\_1. ghrwage[\_n-1]

  -  goutph\_1. goutphr[\_n-1]

  -  goutph\_2. goutphr[\_n-2]

  -  lwkhours. log(wkhours)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `earns.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 41 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'earns.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/earns.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='earns.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
