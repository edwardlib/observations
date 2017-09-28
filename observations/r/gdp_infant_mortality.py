# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gdp_infant_mortality(path):
  """GDP and Infant Mortality

  The `UN` data frame has 207 rows and 2 columns. The data are for 1998
  and are from the United Nations; the observations are nations of the
  world. There are some missing data.

  This data frame contains the following columns:

  infant.mortality
      Infant morality rate, infant deaths per 1000 live births.

  gdp
      GDP per capita, in U.S.~dollars.

  United Nations (1998) Social indicators. Originally from
  http://www.un.org/Depts/unsd/social/main.htm but no longer there.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gdp_infant_mortality.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 207 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gdp_infant_mortality.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/UN.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gdp_infant_mortality.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
