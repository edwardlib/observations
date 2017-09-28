# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def downs_bc(path):
  """Incidence of Down's Syndrome in British Columbia

  The `downs.bc` data frame has 30 rows and 3 columns.

  Down's syndrome is a genetic disorder caused by an extra chromosome 21
  or a part of chromosome 21 being translocated to another chromosome. The
  incidence of Down's syndrome is highly dependent on the mother's age and
  rises sharply after age 30. In the 1960's a large scale study of the
  effect of maternal age on the incidence of Down's syndrome was conducted
  at the British Columbia Health Surveillance Registry. These are the data
  which was collected in that study.

  Mothers were classified by age. Most groups correspond to the age in
  years but the first group comprises all mothers with ages in the range
  15-17 and the last is those with ages 46-49. No data for mothers over 50
  or below 15 were collected.

  This data frame contains the following columns:

  `age`
      The average age of all mothers in the age category.

  `m`
      The total number of live births to mothers in the age category.

  `r`
      The number of cases of Down's syndrome.

  The data were obtained from

  Geyer, C.J. (1991) Constrained maximum likelihood exemplified by
  isotonic convex logistic regression. *Journal of the American
  Statistical Association*, **86**, 717–724.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `downs_bc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'downs_bc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/downs.bc.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='downs_bc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
