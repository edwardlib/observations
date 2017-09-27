# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cps_85(path):
  """Data from the 1985 Current Population Survey (CPS85)

  The Current Population Survey (CPS) is used to supplement census
  information between census years. These data consist of a random sample
  of persons from the CPS85, with information on wages and other
  characteristics of the workers, including sex, number of years of
  education, years of work experience, occupational status, region of
  residence and union membership.

  A data frame with 534 observations on the following variables.

  -  `wage` wage (US dollars per hour)

  -  `educ` number of years of education

  -  `race` a factor with levels `NW` (nonwhite) or `W` (white)

  -  `sex` a factor with levels `F` `M`

  -  `hispanic` a factor with levels `Hisp` `NH`

  -  `south` a factor with levels `NS` `S`

  -  `married` a factor with levels `Married` `Single`

  -  `exper` number of years of work experience (inferred from `age`
     and `educ`)

  -  `union` a factor with levels `Not` `Union`

  -  `age` age in years

  -  `sector` a factor with levels `clerical` `const` `manag`
     `manuf` `other` `prof` `sales` `service`

  Data are from http://lib.stat.cmu.edu/DASL.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cps_85.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 534 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cps_85.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/CPS85.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cps_85.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
