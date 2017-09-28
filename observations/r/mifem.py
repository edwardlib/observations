# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mifem(path):
  """Mortality Outcomes for Females Suffering Myocardial Infarction

  The `mifem` data frame has 1295 rows and 10 columns. This is the
  female subset of the 'monica' data frame

  This data frame contains the following columns:

  outcome
      mortality outcome, a factor with levels `live`, `dead`

  age
      age at onset

  yronset
      year of onset

  premi
      previous myocardial infarction event, a factor with levels `y`,
      `n`, `nk` not known

  smstat
      smoking status, a factor with levels `c` current, `x` ex-smoker,
      `n` non-smoker, `nk` not known

  diabetes
      a factor with levels `y`, `n`, `nk` not known

  highbp
      high blood pressure, a factor with levels `y`, `n`, `nk` not
      known

  hichol
      high cholesterol, a factor with levels `y`, `n` `nk` not known

  angina
      a factor with levels `y`, `n`, `nk` not known

  stroke
      a factor with levels `y`, `n`, `nk` not known

  Newcastle (Australia) centre of the Monica project; see the web site
  http://www.ktl.fi/monica

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mifem.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1295 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mifem.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/mifem.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mifem.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
