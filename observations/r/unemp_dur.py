# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def unemp_dur(path):
  """Unemployment Duration

  Journal of Business Economics and Statistics web site :
  http://amstat.tandfonline.com/loi/ubes20

  *number of observations* : 3343

  A time serie containing :

  spell
      length of spell in number of two-week intervals

  censor1
      = 1 if re-employed at full-time job

  censor2
      = 1 if re-employed at part-time job

  censor3
      1 if re-employed but left job: pt-ft status unknown

  censor4
      1 if still jobless

  age
      age

  ui
      = 1 if filed UI claim

  reprate
      eligible replacement rate

  disrate
      eligible disregard rate

  logwage
      log weekly earnings in lost job (1985\\$)

  tenure
      years tenure in lost job

  McCall, B.P. (1996) “Unemployment Insurance Rules, Joblessness, and
  Part-time Work”, *Econometrica*, **64**, 647–682.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `unemp_dur.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3343 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'unemp_dur.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/UnempDur.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='unemp_dur.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
