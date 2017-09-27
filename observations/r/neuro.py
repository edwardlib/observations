# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def neuro(path):
  """Neurophysiological Point Process Data

  `neuro` is a matrix containing times of observed firing of a neuron in
  windows of 250ms either side of the application of a stimulus to a human
  subject. Each row of the matrix is a replication of the experiment and
  there were a total of 469 replicates.

  The data were collected and kindly made available by Dr. S.J. Boniface
  of the Neurophysiology Unit at the Radcliffe Infirmary, Oxford.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `neuro.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 469 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'neuro.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/neuro.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='neuro.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
