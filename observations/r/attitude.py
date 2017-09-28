# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def attitude(path):
  """The Chatterjee–Price Attitude Data

  From a survey of the clerical employees of a large financial
  organization, the data are aggregated from the questionnaires of the
  approximately 35 employees for each of 30 (randomly selected)
  departments. The numbers give the percent proportion of favourable
  responses to seven questions in each department.

  A data frame with 30 observations on 7 variables. The first column are
  the short names from the reference, the second one the variable names in
  the data frame:

  +--------+--------------+-----------+-------------------------------------+
  | Y      | rating       | numeric   | Overall rating                      |
  +--------+--------------+-----------+-------------------------------------+
  | X[1]   | complaints   | numeric   | Handling of employee complaints     |
  +--------+--------------+-----------+-------------------------------------+
  | X[2]   | privileges   | numeric   | Does not allow special privileges   |
  +--------+--------------+-----------+-------------------------------------+
  | X[3]   | learning     | numeric   | Opportunity to learn                |
  +--------+--------------+-----------+-------------------------------------+
  | X[4]   | raises       | numeric   | Raises based on performance         |
  +--------+--------------+-----------+-------------------------------------+
  | X[5]   | critical     | numeric   | Too critical                        |
  +--------+--------------+-----------+-------------------------------------+
  | X[6]   | advancel     | numeric   | Advancement                         |
  +--------+--------------+-----------+-------------------------------------+

  Chatterjee, S. and Price, B. (1977) *Regression Analysis by Example*.
  New York: Wiley. (Section 3.7, p.68ff of 2nd ed.(1991).)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `attitude.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'attitude.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/attitude.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='attitude.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
