# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def science(path):
  """School Science Survey Data

  The `science` data frame has 1385 rows and 7 columns.

  The data are on attitudes to science, from a survey where there were
  results from 20 classes in private schools and 46 classes in public
  schools.

  This data frame contains the following columns:

  State
      a factor with levels `ACT` Australian Capital Territory, `NSW`
      New South Wales

  PrivPub
      a factor with levels `private` school, `public` school

  school
      a factor, coded to identify the school

  class
      a factor, coded to identify the class

  sex
      a factor with levels `f`, `m`

  like
      a summary score based on two of the questions, on a scale from 1
      (dislike) to 12 (like)

  Class
      a factor with levels corresponding to each class

  Francine Adams, Rosemary Martin and Murali Nayadu, Australian National
  University

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `science.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1385 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'science.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/science.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='science.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
