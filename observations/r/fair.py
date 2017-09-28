# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fair(path):
  """Extramarital Affairs Data

  a cross-section

  *number of observations* : 601

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  sex
      a factor with levels (male,female)

  age
      age

  ym
      number of years married

  child
      children ? a factor

  religious
      how religious, from 1 (anti) to 5 (very)

  education
      education

  occupation
      occupation, from 1 to 7, according to hollingshead classification
      (reverse numbering)

  rate
      self rating of marriage, from 1 (very unhappy) to 5 (very happy)

  nbaffairs
      number of affairs in past year

  Fair, R. (1977) “A note on the computation of the tobit estimator”,
  *Econometrica*, **45**, 1723-1727.

  http://fairmodel.econ.yale.edu/rayfair/pdf/1978A200.PDF.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fair.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 601 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fair.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Fair.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fair.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
