# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cushny(path):
  """Cushny and Peebles Prolongation of Sleep Data

  The original data set was bivariate and recorded for ten subjects the
  prolongation of sleep caused by two different drugs. These data were
  used by Student as the first illustration of the paired t-test which
  only needs the *differences* of the two measurements. These differences
  are the values of `cushny`.

  | numeric vector, sorted increasingly:
  | 0 0.8 1 1.2 1.3 1.3 1.4 1.8 2.4 4.6

  Cushny, A.R. and Peebles, A.R. (1905) The action of optical isomers. II.
  Hyoscines. *J. Physiol.* **32**, 501–510.

  These data were used by Student(1908) as the first illustration of the
  paired t-test, see also `sleep`; then cited by Fisher (1925) and
  thereforth copied in numerous books as an example of a normally
  distributed sample, see, e.g., Anderson (1958).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cushny.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cushny.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/cushny.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cushny.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
