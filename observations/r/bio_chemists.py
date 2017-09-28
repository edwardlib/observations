# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bio_chemists(path):
  """article production by graduate students in biochemistry Ph.D. programs

  A sample of 915 biochemistry graduate students.

  `art`
      count of articles produced during last 3 years of Ph.D.

  `fem`
      factor indicating gender of student, with levels Men and Women

  `mar`
      factor indicating marital status of student, with levels Single and
      Married

  `kid5`
      number of children aged 5 or younger

  `phd`
      prestige of Ph.D. department

  `ment`
      count of articles produced by Ph.D. mentor during last 3 years

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bio_chemists.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 915 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bio_chemists.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/bioChemists.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bio_chemists.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
