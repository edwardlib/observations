# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_judge_ratings(path):
  """Lawyers' Ratings of State Judges in the US Superior Court

  Lawyers' ratings of state judges in the US Superior Court.

  A data frame containing 43 observations on 12 numeric variables.

  +---------+--------+--------------------------------------------+
  | [,1]    | CONT   | Number of contacts of lawyer with judge.   |
  +---------+--------+--------------------------------------------+
  | [,2]    | INTG   | Judicial integrity.                        |
  +---------+--------+--------------------------------------------+
  | [,3]    | DMNR   | Demeanor.                                  |
  +---------+--------+--------------------------------------------+
  | [,4]    | DILG   | Diligence.                                 |
  +---------+--------+--------------------------------------------+
  | [,5]    | CFMG   | Case flow managing.                        |
  +---------+--------+--------------------------------------------+
  | [,6]    | DECI   | Prompt decisions.                          |
  +---------+--------+--------------------------------------------+
  | [,7]    | PREP   | Preparation for trial.                     |
  +---------+--------+--------------------------------------------+
  | [,8]    | FAMI   | Familiarity with law.                      |
  +---------+--------+--------------------------------------------+
  | [,9]    | ORAL   | Sound oral rulings.                        |
  +---------+--------+--------------------------------------------+
  | [,10]   | WRIT   | Sound written rulings.                     |
  +---------+--------+--------------------------------------------+
  | [,11]   | PHYS   | Physical ability.                          |
  +---------+--------+--------------------------------------------+
  | [,12]   | RTEN   | Worthy of retention.                       |
  +---------+--------+--------------------------------------------+

  New Haven Register, 14 January, 1977 (from John Hartigan).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_judge_ratings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 43 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_judge_ratings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/USJudgeRatings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_judge_ratings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
