# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bladdercancer(path):
  """Bladder Cancer Data

  Data arise from 31 male patients who have been treated for superficial
  bladder cancer, and give the number of recurrent tumours during a
  particular time after the removal of the primary tumour, along with the
  size of the original tumour.

  A data frame with 31 observations on the following 3 variables.

  `time`
      the duration.

  `tumorsize`
      a factor with levels `<=3cm` and `>3cm`.

  `number`
      number of recurrent tumours.

  G. U. H. Seeber (1998), Poisson Regression. In: *Encyclopedia of
  Biostatistics* (P. Armitage and T. Colton, eds), John Wiley \\& Sons,
  Chichester.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bladdercancer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 31 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bladdercancer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/bladdercancer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bladdercancer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
