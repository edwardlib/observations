# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def prestige(path):
  """Prestige of Canadian Occupations

  The `Prestige` data frame has 102 rows and 6 columns. The observations
  are occupations.

  This data frame contains the following columns:

  education
      Average education of occupational incumbents, years, in 1971.

  income
      Average income of incumbents, dollars, in 1971.

  women
      Percentage of incumbents who are women.

  prestige
      Pineo-Porter prestige score for occupation, from a social survey
      conducted in the mid-1960s.

  census
      Canadian Census occupational code.

  type
      Type of occupation. A factor with levels (note: out of order):
      `bc`, Blue Collar; `prof`, Professional, Managerial, and
      Technical; `wc`, White Collar.

  Canada (1971) *Census of Canada*. Vol. 3, Part 6. Statistics Canada [pp.
  19-1–19-21].

  Personal communication from B. Blishen, W. Carroll, and C. Moore,
  Departments of Sociology, York University and University of Victoria.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `prestige.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 102 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'prestige.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Prestige.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='prestige.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
