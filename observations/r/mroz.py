# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mroz(path):
  """U.S. Women's Labor-Force Participation

  The `Mroz` data frame has 753 rows and 8 columns. The observations,
  from the Panel Study of Income Dynamics (PSID), are married women.

  This data frame contains the following columns:

  lfp
      labor-force participation; a factor with levels: `no`; `yes`.

  k5
      number of children 5 years old or younger.

  k618
      number of children 6 to 18 years old.

  age
      in years.

  wc
      wife's college attendance; a factor with levels: `no`; `yes`.

  hc
      husband's college attendance; a factor with levels: `no`; `yes`.

  lwg
      log expected wage rate; for women in the labor force, the actual
      wage rate; for women not in the labor force, an imputed value based
      on the regression of `lwg` on the other variables.

  inc
      family income exclusive of wife's income.

  Mroz, T. A. (1987) The sensitivity of an empirical model of married
  women's hours of work to economic and statistical assumptions.
  *Econometrica* **55**, 765–799.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mroz.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 753 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mroz.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Mroz.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mroz.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
