# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gehan(path):
  """Remission Times of Leukaemia Patients

  A data frame from a trial of 42 leukaemia patients. Some were treated
  with the drug *6-mercaptopurine* and the rest are controls. The trial
  was designed as matched pairs, both withdrawn from the trial when either
  came out of remission.

  This data frame contains the following columns:

  `pair`
      label for pair.

  `time`
      remission time in weeks.

  `cens`
      censoring, 0/1.

  `treat`
      treatment, control or 6-MP.

  Cox, D. R. and Oakes, D. (1984) *Analysis of Survival Data.* Chapman &
  Hall, p. 7. Taken from

  Gehan, E.A. (1965) A generalized Wilcoxon test for comparing arbitrarily
  single-censored samples. *Biometrika* **52**, 203–233.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gehan.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 42 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gehan.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/gehan.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gehan.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
