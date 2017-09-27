# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def anorexia(path):
  """Anorexia Data on Weight Change

  The `anorexia` data frame has 72 rows and 3 columns. Weight change
  data for young female anorexia patients.

  This data frame contains the following columns:

  `Treat`
      Factor of three levels: `"Cont"` (control), `"CBT"` (Cognitive
      Behavioural treatment) and `"FT"` (family treatment).

  `Prewt`
      Weight of patient before study period, in lbs.

  `Postwt`
      Weight of patient after study period, in lbs.

  Hand, D. J., Daly, F., McConway, K., Lunn, D. and Ostrowski, E. eds
  (1993) *A Handbook of Small Data Sets.* Chapman & Hall, Data set 285 (p.
  229)

  (Note that the original source mistakenly says that weights are in kg.)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `anorexia.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'anorexia.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/anorexia.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='anorexia.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
