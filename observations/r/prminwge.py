# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def prminwge(path):
  """prminwge

  Data loads lazily. Type data(prminwge) into the console.

  A data.frame with 38 rows and 25 variables:

  -  year. 1950-1987

  -  avgmin. weighted avg min wge, 44 indust

  -  avgwage. wghted avg hrly wge, 44 indust

  -  kaitz. Kaitz min wage index

  -  avgcov. wghted avg coverage, 8 indust

  -  covt. economy-wide coverage of min wg

  -  mfgwage. avg manuf. wage

  -  prdef. Puerto Rican price deflator

  -  prepop. PR employ/popul ratio

  -  prepopf. PR employ/popul ratio, alter.

  -  prgnp. PR GNP

  -  prunemp. PR unemployment rate

  -  usgnp. US GNP

  -  t. time trend: 1 to 38

  -  post74. time trend: starts in 1974

  -  lprunemp. log(prunemp)

  -  lprgnp. log(prgnp)

  -  lusgnp. log(usgnp)

  -  lkaitz. log(kaitz)

  -  lprun\_1. lprunemp[\_n-1]

  -  lprepop. log(prepop)

  -  lprep\_1. lprepop[\_n-1]

  -  mincov. (avgmin/avgwage)\*avgcov

  -  lmincov. log(mincov)

  -  lavgmin. log(avgmin)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `prminwge.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 25 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'prminwge.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/prminwge.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='prminwge.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
