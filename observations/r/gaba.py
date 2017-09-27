# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gaba(path):
  """Effect of pentazocine on post-operative pain (average VAS scores)

  The table shows, separately for males and females, the effect of
  pentazocine on post-operative pain profiles (average VAS scores), with
  (mbac and fbac) and without (mpl and fpl) preoperatively administered
  baclofen. Pain scores are recorded every 20 minutes, from 10 minutes to
  170 minutes.

  A data frame with 9 observations on the following 7 variables.

  `min`
      a numeric vector

  `mbac`
      a numeric vector

  `mpl`
      a numeric vector

  `fbac`
      a numeric vector

  `fpl`
      a numeric vector

  `avbac`
      a numeric vector

  `avplac`
      a numeric vector

  Gordon, N. C. et al.(1995): 'Enhancement of Morphine Analgesia by the
  GABA\ *\_B* against Baclofen'. *Neuroscience* 69: 345-349.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gaba.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gaba.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/gaba.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gaba.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
