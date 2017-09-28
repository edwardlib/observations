# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def arthritis(path):
  """Arthritis Treatment Data

  Data from Koch \\& Edwards (1988) from a double-blind clinical trial
  investigating a new treatment for rheumatoid arthritis.

  A data frame with 84 observations and 5 variables.

  ID
      patient ID.

  Treatment
      factor indicating treatment (Placebo, Treated).

  Sex
      factor indicating sex (Female, Male).

  Age
      age of patient.

  Improved
      ordered factor indicating treatment outcome (None, Some, Marked).

  Michael Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/arthrit.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `arthritis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 84 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'arthritis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Arthritis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='arthritis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
