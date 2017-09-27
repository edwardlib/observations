# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def medpar(path):
  """medpar

  The US national Medicare inpatient hospital database is referred to as
  the Medpar data, which is prepared yearly from hospital filing records.
  Medpar files for each state are also prepared. The full Medpar data
  consists of 115 variables. The national Medpar has some 14 million
  records, with one record for each hospilitiztion. The data in the medpar
  file comes from 1991 Medicare files for the state of Arizona. The data
  are limited to only one diagnostic group (DRG 112). Patient data have
  been randomly selected from the original data.

  A data frame with 1495 observations on the following 10 variables.

  `los`
      length of hospital stay

  `hmo`
      Patient belongs to a Health Maintenance Organization, binary

  `white`
      Patient identifies themselves as Caucasian, binary

  `died`
      Patient died, binary

  `age80`
      Patient age 80 and over, binary

  `type`
      Type of admission, categorical

  `type1`
      Elective admission, binary

  `type2`
      Urgent admission,binary

  `type3`
      Elective admission, binary

  `provnum`
      Provider ID

  1991 National Medpar data, National Health Economics & Research Co.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `medpar.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1495 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'medpar.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/medpar.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='medpar.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
