# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def spam7(path):
  """Spam E-mail Data

  The data consist of 4601 email items, of which 1813 items were
  identified as spam.

  This data frame contains the following columns:

  crl.tot
      total length of words in capitals

  dollar
      number of occurrences of the \\$ symbol

  bang
      number of occurrences of the ! symbol

  money
      number of occurrences of the word ‘money’

  n000
      number of occurrences of the string ‘000’

  make
      number of occurrences of the word ‘make’

  yesno
      outcome variable, a factor with levels `n` not spam, `y` spam

  George Forman, Hewlett-Packard Laboratories

  These data are available from the University of California at Irvine
  Repository of Machine Learning Databases and Domain Theories. The
  address is: http://www.ics.uci.edu/~Here

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `spam7.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4601 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'spam7.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/spam7.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='spam7.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
