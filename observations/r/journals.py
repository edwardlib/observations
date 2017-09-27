# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def journals(path):
  """Economic Journals Dat Set

  a cross-section from 2000

  *number of observations* : 180

  *observation* : goods

  A dataframe containing :

  title
      journal title

  pub
      publisher

  society
      scholarly society ?

  libprice
      library subscription price

  pages
      number of pages

  charpp
      characters per page

  citestot
      total number of citations

  date1
      year journal was founded

  oclc
      number of library subscriptions

  field
      field description

  Professor Theodore Bergstrom of the Department of Economics at the
  University of California, San Diego.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `journals.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 180 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'journals.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Journals.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='journals.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
