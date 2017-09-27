# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fgl(path):
  """Measurements of Forensic Glass Fragments

  The `fgl` data frame has 214 rows and 10 columns. It was collected by
  B. German on fragments of glass collected in forensic work.

  This data frame contains the following columns:

  `RI`
      refractive index; more precisely the refractive index is 1.518xxxx.

      The next 8 measurements are percentages by weight of oxides.

  `Na`
      sodium.

  `Mg`
      manganese.

  `Al`
      aluminium.

  `Si`
      silicon.

  `K`
      potassium.

  `Ca`
      calcium.

  `Ba`
      barium.

  `Fe`
      iron.

  `type`
      The fragments were originally classed into seven types, one of which
      was absent in this dataset. The categories which occur are window
      float glass (`WinF`: 70), window non-float glass (`WinNF`: 76),
      vehicle window glass (`Veh`: 17), containers (`Con`: 13),
      tableware (`Tabl`: 9) and vehicle headlamps (`Head`: 29).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fgl.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 214 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fgl.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/fgl.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fgl.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
