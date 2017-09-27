# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def child_speaks(path):
  """ChildSpeaks

  Age at first speaking and aptitude test scores

  A dataset with 21 observations on the following 3 variables.

  `Child`

  ID for each child

  `Age`

  Age at first speaking (in months)

  `Gesell`

  Gesell Aptitude Test Score

  These data were originally collected by L.M. Linde of UCLA but were
  first published by M.R. Mickey, O.J. Dunn, and V. Clark, "Note on the
  use of stepwise regression in detecting outliers," Computers and
  Biomedical Research, 1 (1967), pp. 105-111. The data have been used by
  several authors. We found them in David Moore's Basic Practice of

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `child_speaks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'child_speaks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/ChildSpeaks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='child_speaks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
