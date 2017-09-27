# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def loomis(path):
  """loomis

  Data are taken from Loomis (2003). The study relates to a survey taken
  on reported frequency of visits to national parks during the year. The
  survey was taken at park sites, thus incurring possible effects of
  endogenous stratification.

  A data frame with 410 observations on the following 11 variables.

  `anvisits`
      number of annual visits to park

  `gender`
      1=male;0=female

  `income`
      income in US dollars per year, categorical: 4 levels

  `income1`
      <=$25000

  `income2`
      >$25000 - $55000

  `income3`
      >$55000 - $95000

  `income4`
      >$95000

  `travel`
      travel time, categorical: 3 levels

  `travel1`
      <.25 hrs

  `travel2`
      >=.25 - <4 hrs

  `travel3`
      >=4 hrs

  from Loomis (2003)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `loomis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 410 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'loomis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/loomis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='loomis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
