# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def states(path):
  """Education and Related Statistics for the U.S. States

  The `States` data frame has 51 rows and 8 columns. The observations
  are the U. S. states and Washington, D. C.

  This data frame contains the following columns:

  region
      U. S. Census regions. A factor with levels: `ENC`, East North
      Central; `ESC`, East South Central; `MA`, Mid-Atlantic; `MTN`,
      Mountain; `NE`, New England; `PAC`, Pacific; `SA`, South
      Atlantic; `WNC`, West North Central; `WSC`, West South Central.

  pop
      Population: in 1,000s.

  SATV
      Average score of graduating high-school students in the state on the
      *verbal* component of the Scholastic Aptitude Test (a standard
      university admission exam).

  SATM
      Average score of graduating high-school students in the state on the
      *math* component of the Scholastic Aptitude Test.

  percent
      Percentage of graduating high-school students in the state who took
      the SAT exam.

  dollars
      State spending on public education, in \\$1000s per student.

  pay
      Average teacher's salary in the state, in $1000s.

  United States (1992) *Statistical Abstract of the United States.* Bureau
  of the Census.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `states.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'states.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/States.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='states.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
