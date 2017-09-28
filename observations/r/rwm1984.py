# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rwm1984(path):
  """rwm1984

  German health registry for the year 1984.

  A data frame with 3,874 observations on the following 17 variables.

  `docvis`
      number of visits to doctor during year (0-121)

  `hospvis`
      number of days in hospital during year (0-51)

  `edlevel`
      educational level (categorical: 1-4)

  `age`
      age: 25-64

  `outwork`
      out of work=1; 0=working

  `female`
      female=1; 0=male

  `married`
      married=1; 0=not married

  `kids`
      have children=1; no children=0

  `hhninc`
      household yearly income in marks (in Marks)

  `educ`
      years of formal education (7-18)

  `self`
      self-employed=1; not self employed=0

  `edlevel1`
      (1/0) not high school graduate

  `edlevel2`
      (1/0) high school graduate

  `edlevel3`
      (1/0) university/college

  `edlevel4`
      (1/0) graduate school

  German Health Reform Registry, year=1984, in Hilbe and Greene (2007)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rwm1984.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3874 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rwm1984.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/rwm1984.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rwm1984.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
