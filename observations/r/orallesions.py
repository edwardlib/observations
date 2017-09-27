# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def orallesions(path):
  """Oral Lesions in Rural India

  The distribution of the oral lesion site found in house-to-house surveys
  in three geographic regions of rural India.

  A two-way classification, see `table`.

  Cyrus R. Mehta and Nitin R. Patel (2003), *StatXact-6: Statistical
  Software for Exact Nonparametric Inference*, Cytel Software Cooperation,
  Cambridge, USA.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `orallesions.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'orallesions.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/orallesions.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='orallesions.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
