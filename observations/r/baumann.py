# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def baumann(path):
  """Methods of Teaching Reading Comprehension

  The `Baumann` data frame has 66 rows and 6 columns. The data are from
  an experimental study conducted by Baumann and Jones, as reported by
  Moore and McCabe (1993) Students were randomly assigned to one of three
  experimental groups.

  This data frame contains the following columns:

  group
      Experimental group; a factor with levels: `Basal`, traditional
      method of teaching; `DRTA`, an innovative method; `Strat`,
      another innovative method.

  pretest.1
      First pretest.

  pretest.2
      Second pretest.

  post.test.1
      First post-test.

  post.test.2
      Second post-test.

  post.test.3
      Third post-test.

  Moore, D. S. and McCabe, G. P. (1993) *Introduction to the Practice of
  Statistics, Second Edition.* Freeman, p. 794–795.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `baumann.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 66 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'baumann.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Baumann.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='baumann.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
