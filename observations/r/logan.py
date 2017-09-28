# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def logan(path):
  """Data from the 1972-78 GSS data used by Logan

  Intergenerational occupational mobility data with covariates.

  A data frame with 838 observations on the following 4 variables.

  occupation
      subject's occupation, a factor with levels `farm`, `operatives`,
      `craftsmen`, `sales`, and `professional`

  focc
      father's occupation

  education
      total years of schooling, 0 to 20

  race
      levels of `non-black` and `black`

  General Social Survey data, see the web site for detailed information on
  the variables. http://www3.norc.org/GSS+Website.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `logan.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 838 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'logan.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/logan.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='logan.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
