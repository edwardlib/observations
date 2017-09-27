# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def visual_acuity(path):
  """Visual Acuity in Left and Right Eyes

  Data from Kendall & Stuart (1961) on unaided vision among 3,242 men and
  7,477 women, all aged 30-39 and employed in the U.K. Royal Ordnance
  factories 1943-1946.

  A data frame with 32 observations and 4 variables.

  Freq
      frequency of visual acuity measurements.

  right
      visual acuity on right eye.

  left
      visual acuity on left eye.

  gender
      factor indicating gender of patient.

  M. Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/vision.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `visual_acuity.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'visual_acuity.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/VisualAcuity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='visual_acuity.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
