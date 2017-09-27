# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nidd(path):
  """Rain, wavesurge, portpirie and nidd datasets.

  Rainfall, wave-surge, Port Pirie and River Nidd data sets.

  The format of the rain data is: num [1:17531] 0 2.3 1.3 6.9 4.6 0 1 1.5
  1.8 1.8 ...

  The wave-surge data is bivariate and is used for testing functions in
  `texmex`.

  The Port Pirie data has two columns: 'Year' and 'SeaLevel'.

  The River Nidd data represents 154 measurements of the level of the
  River Nidd at Hunsingore Weir (Yorkshire, UK) between 1934 and 1969.
  Each measurement breaches the threshold of $65 m^3/2$. Various authors
  have analysed this dataset, as described by Papastathopoulos and
  Tawn~egp, there being some apparent difficulty in identifying a
  threshold above which GPD models are suitable.

  Copied from the `ismev` package and the `evir` package

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nidd.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 154 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nidd.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/texmex/nidd.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nidd.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
