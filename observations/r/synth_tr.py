# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def synth_tr(path):
  """Synthetic Classification Problem

  The `synth.tr` data frame has 250 rows and 3 columns. The `synth.te`
  data frame has 100 rows and 3 columns. It is intended that `synth.tr`
  be used from training and `synth.te` for testing.

  These data frames contains the following columns:

  `xs`
      x-coordinate

  `ys`
      y-coordinate

  `yc`
      class, coded as 0 or 1.

  Ripley, B.D. (1994) Neural networks and related methods for
  classification (with discussion). *Journal of the Royal Statistical
  Society series B* **56**, 409–456.

  Ripley, B.D. (1996) *Pattern Recognition and Neural Networks.*

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `synth_tr.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 250 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'synth_tr.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/synth.tr.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='synth_tr.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
