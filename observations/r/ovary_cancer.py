# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ovary_cancer(path):
  """Ovary Cancer Data

  Data from Obel (1975) about a retrospective study of ovary cancer
  carried out in 1973. Information was obtained from 299 women, who were
  operated for ovary cancer 10 years before.

  A data frame with 16 observations and 5 variables.

  Freq
      frequency.

  stage
      factor indicating the stage of the cancer at the time of operation
      (early, advanced).

  operation
      factor indicating type of operation (radical, limited).

  survival
      factor indicating survival status after 10 years (yes, no).

  xray
      factor indicating whether X-ray treatment was received (yes, no).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  Table 6.4.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ovary_cancer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ovary_cancer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/OvaryCancer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ovary_cancer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
