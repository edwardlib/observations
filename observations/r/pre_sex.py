# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pre_sex(path):
  """Pre-marital Sex and Divorce

  Data from Thornes \\& Collard (1979), reported in Gilbert (1981), on
  pre- and extra-marital sex and divorce.

  A 4-dimensional array resulting from cross-tabulating 1036 observations
  on 4 variables. The variables and their levels are as follows:

  +------+-------------------+---------------------+
  | No   | Name              | Levels              |
  +------+-------------------+---------------------+
  | 1    | MaritalStatus     | Divorced, Married   |
  +------+-------------------+---------------------+
  | 2    | ExtramaritalSex   | Yes, No             |
  +------+-------------------+---------------------+
  | 3    | PremaritalSex     | Yes, No             |
  +------+-------------------+---------------------+
  | 4    | Gender            | Women, Men          |
  +------+-------------------+---------------------+

  Michael Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/marital.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pre_sex.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pre_sex.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/PreSex.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pre_sex.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
