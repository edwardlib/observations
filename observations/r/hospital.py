# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hospital(path):
  """Hospital data

  The table relates the length of stay (in years) of 132 long-term
  schizophrenic patients in two London mental hospitals with the frequency
  of visits.

  A 2-dimensional array resulting from cross-tabulating 132 patients. The
  variables and their levels are as follows:

  +------+-------------------+---------------------------------------+
  | No   | Name              | Levels                                |
  +------+-------------------+---------------------------------------+
  | 1    | Visit Frequency   | Regular, Less than monthly, Never     |
  +------+-------------------+---------------------------------------+
  | 2    | Length of Stay    | 2--9 years, 10--19 years, 20+ years   |
  +------+-------------------+---------------------------------------+

  S.J Haberman (1974): Log-linear models for frequency tables with ordered
  classifications. Biometrics, 30:689–700.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hospital.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hospital.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Hospital.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hospital.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
