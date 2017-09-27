# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def toothpaste(path):
  """Toothpaste Data

  Meta-analysis of studies comparing two different toothpastes.

  A data frame with 9 observations on the following 7 variables.

  `Study`
      the identifier of the study.

  `nA`
      number of subjects using toothpaste A.

  `meanA`
      mean DMFS index of subjects using toothpaste A.

  `sdA`
      standard deviation of DMFS index of subjects using toothpaste A.

  `nB`
      number of subjects using toothpaste B.

  `meanB`
      mean DMFS index of subjects using toothpaste B.

  `sdB`
      standard deviation of DMFS index of subjects using toothpaste B.

  B. S. Everitt and A. Pickles (2000), *Statistical Aspects of the Design
  and Analysis of Clinical Trials*, Imperial College Press, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `toothpaste.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'toothpaste.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/toothpaste.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='toothpaste.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
