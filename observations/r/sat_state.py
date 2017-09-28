# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sat_state(path):
  """State by State SAT data

  SAT data assembled for a statistics education journal article on the
  link between SAT scores and measures of educational expenditures

  A data frame with 50 observations on the following variables.

  -  `state` a factor with names of each state

  -  `expend` expenditure per pupil in average daily attendance in
     public elementary and secondary schools, 1994-95 (in thousands of US
     dollars)

  -  `ratio` average pupil/teacher ratio in public elementary and
     secondary schools, Fall 1994

  -  `salary` estimated average annual salary of teachers in public
     elementary and secondary schools, 1994-95 (in thousands of US
     dollars)

  -  `frac` percentage of all eligible students taking the SAT, 1994-95

  -  `verbal` average verbal SAT score, 1994-95

  -  `math` average math SAT score, 1994-95

  -  `sat` average total SAT score, 1994-95

  http://www.amstat.org/publications/jse/secure/v7n2/datasets.guber.cfm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sat_state.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sat_state.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/SAT.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sat_state.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
