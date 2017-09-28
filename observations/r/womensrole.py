# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def womensrole(path):
  """Womens Role in Society

  Data from a survey from 1974 / 1975 asking both female and male
  responders about their opinion on the statement: Women should take care
  of running their homes and leave running the country up to men.

  A data frame with 42 observations on the following 4 variables.

  `education`
      years of education.

  `sex`
      a factor with levels `Male` and `Female`.

  `agree`
      number of subjects in agreement with the statement.

  `disagree`
      number of subjects in disagreement with the statement.

  S. J. Haberman (1973), The analysis of residuals in cross-classificed
  tables. *Biometrics*, **29**, 205–220.

  D. Collett (2003), *Modelling Binary Data*. Chapman and Hall / CRC,
  London. 2nd edition.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `womensrole.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 42 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'womensrole.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/womensrole.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='womensrole.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
