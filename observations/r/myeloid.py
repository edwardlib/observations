# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def myeloid(path):
  """Acute myeloid leukemia

  This simulated data set is based on a trial in acute myeloid leukemia.

  A data frame with 646 observations on the following 9 variables.

  `id`
      subject identifier, 1-646

  `trt`
      treatment arm A or B

  `futime`
      time to death or last follow-up

  `death`
      1 if `futime` is a death, 0 for censoring

  `txtime`
      time to hematropetic stem cell transplant

  `crtime`
      time to complete response

  `rltime`
      time to relapse of disease

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `myeloid.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 646 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'myeloid.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/myeloid.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='myeloid.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
