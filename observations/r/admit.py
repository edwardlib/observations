# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def admit(path):
  """Applications to a Political Science PhD Program

  Ordinal ratings (faculty evaluations) of applicants to a Political
  Science PhD Program.

  A data frame with 106 observations on the following 6 variables.

  `score`
      an ordered factor with levels `1` < `2` < `3` < `4` < `5`

  `gre.quant`
      applicant's score on the quantitative section of the GRE; the
      maximum score is 800

  `gre.verbal`
      applicant's score on the verbal section of the GRE; the maximum
      score is 800

  `ap`
      1 if the applicant indicated an interest in American politics; 0
      otherwise

  `pt`
      1 if the applicant indicated an interest in Political Theory; 0
      otherwise

  `female`
      1 for female applicants; 0 otherwise

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `admit.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 106 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'admit.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/admit.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='admit.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
