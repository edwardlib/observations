# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def minwage(path):
  """minwage

  Data loads lazily. Type data(minwage) into the console.

  A data.frame with 612 rows and 58 variables:

  -  emp232. employment, sector 232, 1000s

  -  wage232. hourly wage, sector 232, $

  -  emp236.

  -  wage236.

  -  emp234.

  -  wage234.

  -  emp314.

  -  wage314.

  -  emp228.

  -  wage228.

  -  emp233.

  -  wage233.

  -  emp394.

  -  wage394.

  -  emp231.

  -  wage231.

  -  emp226.

  -  wage226.

  -  emp387.

  -  wage387.

  -  emp056.

  -  wage056.

  -  unem. civilian unemployment rate, percent

  -  cpi. Consumer Price Index (urban), 1982-1984 = 100

  -  minwage. Federal minimum wage, $/hour

  -  lemp232. log(emp232)

  -  lwage232. log(wage232)

  -  gemp232. lemp232 - lemp232[\_n-1]

  -  gwage232. lwage232 - lwage232[\_n-1]

  -  lminwage. log(minwage)

  -  gmwage. lminwage - lminwage[\_n-1]

  -  gmwage\_1. gmwage[\_n-1]

  -  gmwage\_2.

  -  gmwage\_3.

  -  gmwage\_4.

  -  gmwage\_5.

  -  gmwage\_6.

  -  gmwage\_7.

  -  gmwage\_8.

  -  gmwage\_9.

  -  gmwage\_10.

  -  gmwage\_11.

  -  gmwage\_12.

  -  lemp236.

  -  gcpi. lcpi - lcpi[\_n-1]

  -  lcpi. log(cpi)

  -  lwage236.

  -  gemp236.

  -  gwage236.

  -  lemp234.

  -  lwage234.

  -  gemp234.

  -  gwage234.

  -  lemp314.

  -  lwage314.

  -  gemp314.

  -  gwage314.

  -  t. linear time trend, 1 to 612

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `minwage.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 612 rows and 58 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'minwage.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/minwage.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='minwage.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
