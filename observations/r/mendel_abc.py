# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mendel_abc(path):
  """Mendel's F2 trifactorial data

  The `mendel3` data frame has 27 rows and 4 columns. Data are from
  Mendel (1886), and are reproduced in Fisher (1936) and Weir (1996).

  ABC:
  Seed Shape      (A: round or wrinkled)
  Cotyledon Color (B: albumen yellow or green)
  Seed Coat Color (C: grey-brown or white)


  This data frame contains the following columns:

  seedshape
      Factor with levels: `AA`, `Aa` and `aa`

  cotylcolor
      Factor with levels: `BB`, `Bb` and `bb`

  coatcolor
      Factor with levels: `CC`, `Cc` and `cc`

  Observed
      a numeric vector that holds the frequencies.

  Data are from Mendel (1886), and are reproduced in Fisher (1936) and
  Weir (1996).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mendel_abc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mendel_abc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/hwde/mendelABC.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mendel_abc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
