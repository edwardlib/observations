# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def acf1(path):
  """Aberrant Crypt Foci in Rat Colons

  Numbers of aberrant crypt foci (ACF) in the section 1 of the colons of
  22 rats subjected to a single dose of the carcinogen azoxymethane (AOM),
  sacrificed at 3 different times.

  This data frame contains the following columns:

  count
      The number of ACF observed in section 1 of each rat colon

  endtime
      Time of sacrifice, in weeks following injection of AOM

  Ranjana P. Bird, Faculty of Human Ecology, University of Manitoba,
  Winnipeg, Canada.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `acf1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'acf1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/ACF1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='acf1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
