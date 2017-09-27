# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def jobs(path):
  """Canadian Labour Force Summary Data (1995-96)

  The number of workers in the Canadian labour force broken down by region
  (BC, Alberta, Prairies, Ontario, Quebec, Atlantic) for the 24-month
  period from January, 1995 to December, 1996 (a time when Canada was
  emerging from a deep economic recession).

  This data frame contains the following columns:

  BC
      monthly labour force counts in British Columbia

  Alberta
      monthly labour force counts in Alberta

  Prairies
      monthly labour force counts in Saskatchewan and Manitoba

  Ontario
      monthly labour force counts in Ontario

  Quebec
      monthly labour force counts in Quebec

  Atlantic
      monthly labour force counts in Newfoundland, Nova Scotia, Prince
      Edward Island and New Brunswick

  Date
      year (in decimal form)

  Statistics Canada

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `jobs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 899 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'jobs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/jobs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='jobs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
