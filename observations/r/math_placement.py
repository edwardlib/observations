# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def math_placement(path):
  """Math Placement

  Results from a Math Placement exam at a liberal arts college

  A dataset with 2696 observations on the following 16 variables.

  `Student`

  Identification number for each student

  `Gender`

  0=Female, 1=Male

  `PSATM`

  PSAT score in MAth

  `SATM`

  SAT score in Math

  `ACTM`

  ACT Score in Math

  `Rank`

  Adjusted rank in HS class

  `Size`

  Number of students in HS class

  `GPAadj`

  Adjusted GPA

  `PlcmtScore`

  Score on math placement exam

  `Recommends`

  Recommended course: `R0` `R01` `R1` `R12` `R2` `R3` `R4`
  `R6` `R8`

  `Course`

  Actual course taken

  `Grade`

  Course grade

  `RecTaken`

  1=recommended course, 0=otherwise

  `TooHigh`

  1=took course above recommended, 0=otherwise

  `TooLow`

  1=took course below recommended, 0=otherwise

  `CourseSuccess`

  1=B or better grade, 0=grade below B


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `math_placement.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2696 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'math_placement.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MathPlacement.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='math_placement.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
