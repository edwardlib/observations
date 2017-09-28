# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sitka89(path):
  """Growth Curves for Sitka Spruce Trees in 1989

  The `Sitka89` data frame has 632 rows and 4 columns. It gives repeated
  measurements on the log-size of 79 Sitka spruce trees, 54 of which were
  grown in ozone-enriched chambers and 25 were controls. The size was
  measured eight times in 1989, at roughly monthly intervals.

  This data frame contains the following columns:

  `size`
      measured size (height times diameter squared) of tree, on log scale.

  `Time`
      time of measurement in days since 1 January 1988.

  `tree`
      number of tree.

  `treat`
      either `"ozone"` for an ozone-enriched chamber or `"control"`.

  P. J. Diggle, K.-Y. Liang and S. L. Zeger (1994) *Analysis of
  Longitudinal Data.* Clarendon Press, Oxford

  See Also
  ~~~~~~~~


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sitka89.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 632 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sitka89.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Sitka89.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sitka89.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
