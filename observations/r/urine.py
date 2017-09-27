# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def urine(path):
  """Urine Analysis Data

  The `urine` data frame has 79 rows and 7 columns.

  79 urine specimens were analyzed in an effort to determine if certain
  physical characteristics of the urine might be related to the formation
  of calcium oxalate crystals.

  This data frame contains the following columns:

  `r`
      Indicator of the presence of calcium oxalate crystals.

  `gravity`
      The specific gravity of the urine.

  `ph`
      The pH reading of the urine.

  `osmo`
      The osmolarity of the urine. Osmolarity is proportional to the
      concentration of molecules in solution.

  `cond`
      The conductivity of the urine. Conductivity is proportional to the
      concentration of charged ions in solution.

  `urea`
      The urea concentration in millimoles per litre.

  `calc`
      The calcium concentration in millimoles per litre.

  The data were obtained from

  Andrews, D.F. and Herzberg, A.M. (1985) *Data: A Collection of Problems
  from Many Fields for the Student and Research Worker*. Springer-Verlag.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `urine.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 79 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'urine.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/urine.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='urine.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
