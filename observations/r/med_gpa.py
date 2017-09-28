# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def med_gpa(path):
  """MedGPA

  Medical school admission status and information on GPA and standardized
  test scores

  A dataset with 55 observations on the following 11 variables.

  `Accept`

  Status: `A`\ =accepted to medical school or `D`\ =denied admission

  `Acceptance`

  Indicator for Accept: `1`\ =accepted or `0`\ =denied

  `Sex`

  `F`\ =female or `M`\ =male

  `BCPM`

  Bio/Chem/Physics/Math grade point average

  `GPA`

  College grade point average

  `VR`

  Verbal reasoning (subscore)

  `PS`

  Physical sciences (subscore)

  `WS`

  Writing sample (subcore)

  `BS`

  Biological sciences (subscore)

  `MCAT`

  Score on the MCAT exam (sum of CR+PS+WS+BS)

  `Apps`

  Number of medical schools applied to


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `med_gpa.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 55 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'med_gpa.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MedGPA.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='med_gpa.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
