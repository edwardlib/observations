# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def jevons(path):
  """W. Stanley Jevons' data on numerical discrimination

  In a remarkable brief note in *Nature*, 1871, W. Stanley Jevons
  described the results of an experiment he had conducted on himself to
  determine the limits of the number of objects an observer could
  comprehend immediately without counting them. This was an important
  philosophical question: How many objects can the mind embrace at once?

  He carried out 1027 trials in which he tossed an "uncertain number" of
  uniform black beans into a box and immediately attempted to estimate the
  number "without the least hesitation". His questions, procedure and
  analysis anticipated by 75 years one of the most influential papers in
  modern cognitive psychology by George Miller (1956), "The magical number
  7 plus or minus 2: Some limits on ..." For Jevons, the magical number
  was 4.5, representing an empirical law of complete accuracy.

  A frequency data frame with 50 observations on the following 4
  variables.

  `actual`
      Actual number: a numeric vector

  `estimated`
      Estimated number: a numeric vector

  `frequency`
      Frequency of this combination of (actual, estimated): a numeric
      vector

  `error`
      `actual`-`estimated`: a numeric vector

  Jevons, W. S. (1871). The Power of Numerical Discrimination, *Nature*,
  1871, III (281-282)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `jevons.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'jevons.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Jevons.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='jevons.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
