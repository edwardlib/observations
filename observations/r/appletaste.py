# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def appletaste(path):
  """Tasting experiment that compared four apple varieties

  Each of 20 tasters each assessed three out of the four varieties. The
  experiment was conducted according to a balanced incomplete block
  design.

  A data frame with 60 observations on the following 3 variables.

  aftertaste
      a numeric vector

  Apple samples were rated for `aftertaste`, by making a mark on a
  continuous scale that ranged from 0 (extreme dislike) to 150 (like very
  much).

  panelist
      a factor with levels `a` `b` `c` `d` `e` `f` `g` `h`
      `i` `j` `k` `l` `m` `n` `o` `p` `q` `r` `s`
      `t`

  product
      a factor with levels `298` `493` `649` `937`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `appletaste.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'appletaste.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/appletaste.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='appletaste.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
