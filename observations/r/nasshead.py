# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nasshead(path):
  """Documentation of names of columns in nass9702cor

  `SASname` and `longname` are from the SAS XPT file nass9702cor.XPT
  that is available from the webite noted below. The name `shortname` is
  the name used in the data frame `nass9702cor`, not included in this
  package, but available from my website that is noted below. It is also
  used in `nassCDS`, for columns that `nassCDS` includes.

  A data frame with 56 observations on the following 3 variables.

  `shortname`
      a character vector

  `SASname`
      a character vector

  `longname`
      a character vector

  http://www.stat.colostate.edu/~meyer/airbags.htm\\
  ftp://ftp.nhtsa.dot.gov/nass/\\ Click, e.g., on 1997 and then on
  SASformats. See also http://www.maths.anu.edu.au/~johnm/datasets/airbags

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nasshead.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nasshead.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nasshead.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nasshead.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
