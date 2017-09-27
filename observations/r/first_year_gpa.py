# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def first_year_gpa(path):
  """FirstYearGPA

  Predicting first-year college GPA

  A dataset with 219 observations on the following 10 variables.

  `GPA`

  First-year college GPA on a 0.0-4.0 scale

  `HSGPA`

  High school GPA on a 0.0-4.0 scale

  `SATV`

  Verbal/critical reading SAT score

  `SATM`

  Math SAT score

  `Male`

  `1`\ = male, `0`\ = female

  `HU`

  Number of credit hours earned in humanities courses in high school

  `SS`

  Number of credit hours earned in social science courses in high school

  `FirstGen`

  `1`\ = student is the first in her or his family to attend college,
  `0`\ =otherwise

  `White`

  `1`\ = white students, `0`\ = others

  `CollegeBound`

  `1`\ =attended a high school where >=50% students intended to go on to
  college, `0`\ =otherwise

  A sample from a larger set of data collected in 1996 by a professor at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `first_year_gpa.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 219 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'first_year_gpa.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FirstYearGPA.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='first_year_gpa.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
