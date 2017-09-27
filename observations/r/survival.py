# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def survival(path):
  """Survival of Rats after Radiation Doses

  The `survival` data frame has 14 rows and 2 columns.

  The data measured the survival percentages of batches of rats who were
  given varying doses of radiation. At each of 6 doses there were two or
  three replications of the experiment.

  This data frame contains the following columns:

  `dose`
      The dose of radiation administered (rads).

  `surv`
      The survival rate of the batches expressed as a percentage.

  The data were obtained from

  Efron, B. (1988) Computer-intensive methods in statistical regression.
  *SIAM Review*, **30**, 421–449.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `survival.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'survival.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/survival.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='survival.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
