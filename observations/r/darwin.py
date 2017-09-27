# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def darwin(path):
  """Darwin's Plant Height Differences

  The `darwin` data frame has 15 rows and 1 columns.

  Charles Darwin conducted an experiment to examine the superiority of
  cross-fertilized plants over self-fertilized plants. 15 pairs of plants
  were used. Each pair consisted of one cross-fertilized plant and one
  self-fertilized plant which germinated at the same time and grew in the
  same pot. The plants were measured at a fixed time after planting and
  the difference in heights between the cross- and self-fertilized plants
  are recorded in eighths of an inch.

  This data frame contains the following column:

  `y`
      The difference in heights for the pairs of plants (in units of 0.125
      inches).

  The data were obtained from

  Fisher, R.A. (1935) *Design of Experiments*. Oliver and Boyd.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `darwin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'darwin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/darwin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='darwin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
