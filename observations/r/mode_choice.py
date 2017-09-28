# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mode_choice(path):
  """Data to Study Travel Mode Choice

  a cross-section

  *number of observations* : 840

  *observation* : individuals

  *country* : Australia

  A dataframe containing :

  mode
      choice : air, train, bus or car

  ttme
      terminal waiting cost time, 0 for car

  invc
      in vehicle cost-cost component

  invt
      travel time in vehicle

  gc
      generalized cost measure

  hinc
      household income

  psize
      party size in mode chosen

  Greene, W.H. and D. Hensher (1997) *Multinomial logit and discrete
  choice models* *in* Greene, W. H. (1997) *LIMDEP version 7.0 user's
  manual revised*, Plainview, New York econometric software, Inc .

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mode_choice.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 840 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mode_choice.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/ModeChoice.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mode_choice.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
