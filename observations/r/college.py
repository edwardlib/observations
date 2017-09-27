# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def college(path):
  """U.S. News and World Report's College Data

  Statistics for a large number of US Colleges from the 1995 issue of US
  News and World Report.

  A data frame with 777 observations on the following 18 variables.

  `Private`
      A factor with levels `No` and `Yes` indicating private or public
      university

  `Apps`
      Number of applications received

  `Accept`
      Number of applications accepted

  `Enroll`
      Number of new students enrolled

  `Top10perc`
      Pct. new students from top 10% of H.S. class

  `Top25perc`
      Pct. new students from top 25% of H.S. class

  `F.Undergrad`
      Number of fulltime undergraduates

  `P.Undergrad`
      Number of parttime undergraduates

  `Outstate`
      Out-of-state tuition

  `Room.Board`
      Room and board costs

  `Books`
      Estimated book costs

  `Personal`
      Estimated personal spending

  `PhD`
      Pct. of faculty with Ph.D.'s

  `Terminal`
      Pct. of faculty with terminal degree

  `S.F.Ratio`
      Student/faculty ratio

  `perc.alumni`
      Pct. alumni who donate

  `Expend`
      Instructional expenditure per student

  `Grad.Rate`
      Graduation rate

  This dataset was taken from the StatLib library which is maintained at
  Carnegie Mellon University. The dataset was used in the ASA Statistical
  Graphics Section's 1995 Data Analysis Exposition.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `college.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 777 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'college.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/College.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='college.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
