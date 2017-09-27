# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tinting(path):
  """Car Window Tinting Experiment Data

  These data are from an experiment that aimed to model the effects of the
  tinting of car windows on visual performance. The authors were mainly
  interested in effects on side window vision, and hence in visual
  recognition tasks that would be performed when looking through side
  windows.

  This data frame contains the following columns:

  case
      observation number

  id
      subject identifier code (1-26)

  age
      age (in years)

  sex
      a factor with levels `f` female, `m` male

  tint
      an ordered factor with levels representing degree of tinting: `no`
      < `lo` < `hi`

  target
      a factor with levels `locon`: low contrast, `hicon`: high
      contrast

  it
      the inspection time, the time required to perform a simple
      discrimination task (in milliseconds)

  csoa
      critical stimulus onset asynchrony, the time to recognize an
      alphanumeric target (in milliseconds)

  agegp
      a factor with levels `younger`, 21-27, `older`, 70-78

  Burns, N.R., Nettlebeck, T., White, M. and Willson, J., 1999. Effects of
  car window tinting on visual performance: a comparison of younger and
  older drivers. Ergonomics 42: 428-443.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tinting.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 182 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tinting.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/tinting.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tinting.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
