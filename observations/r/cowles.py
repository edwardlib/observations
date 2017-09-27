# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cowles(path):
  """Cowles and Davis's Data on Volunteering

  The `Cowles` data frame has 1421 rows and 4 columns. These data come
  from a study of the personality determinants of volunteering for
  psychological research.

  This data frame contains the following columns:

  neuroticism
      scale from Eysenck personality inventory

  extraversion
      scale from Eysenck personality inventory

  sex
      a factor with levels: `female`; `male`

  volunteer
      volunteeing, a factor with levels: `no`; `yes`

  Cowles, M. and C. Davis (1987) The subject matter of psychology:

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cowles.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1421 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cowles.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Cowles.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cowles.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
