# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bacteria(path):
  """Presence of Bacteria after Drug Treatments

  Tests of the presence of the bacteria *H. influenzae* in children with
  otitis media in the Northern Territory of Australia.

  This data frame has 220 rows and the following columns:

  y
      presence or absence: a factor with levels `n` and `y`.

  ap
      active/placebo: a factor with levels `a` and `p`.

  hilo
      hi/low compliance: a factor with levels `hi` amd `lo`.

  week
      numeric: week of test.

  ID
      subject ID: a factor.

  trt
      a factor with levels `placebo`, `drug` and `drug+`, a
      re-coding of `ap` and `hilo`.

  Dr Amanda Leach *via* Mr James McBroom.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bacteria.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 220 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bacteria.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/bacteria.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bacteria.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
