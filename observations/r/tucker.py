# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tucker(path):
  """9 Cognitive variables discussed by Tucker and Lewis (1973)

  Tucker and Lewis (1973) introduced a reliability coefficient for ML
  factor analysis. Their example data set was previously reported by
  Tucker (1958) and taken from Thurstone and Thurstone (1941). The
  correlation matrix is a 9 x 9 for 710 subjects and has two correlated
  factors of ability: Word Fluency and Verbal.

  A data frame with 9 observations on the following 9 variables.

  `t42`
      Prefixes

  `t54`
      Suffixes

  `t45`
      Chicago Reading Test: Vocabulary

  `t46`
      Chicago Reading Test: Sentences

  `t23`
      First and last letters

  `t24`
      First letters

  `t27`
      Four letter words

  `t10`
      Completion

  `t51`
      Same or Opposite

  Tucker, Ledyard (1958) An inter-battery method of factor analysis,
  Psychometrika, 23, 111-136.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tucker.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tucker.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Tucker.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tucker.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
