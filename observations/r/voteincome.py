# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def voteincome(path):
  """Sample Turnout and Demographic Data from the 2000 Current Population Surve
  y

  This data set contains turnout and demographic data from a sample of
  respondents to the 2000 Current Population Survey (CPS). The states
  represented are South Carolina and Arkansas. The data represent only a
  sample and results from this example should not be used in publication.

  A data frame containing 7 variables ("state", "year", "vote", "income",
  "education", "age", "female") and 1500 observations.

  `state`
      a factor variable with levels equal to "AR" (Arkansas) and "SC"
      (South Carolina)

  `year`
      an integer vector

  `vote`
      an integer vector taking on values "1" (Voted) and "0" (Did Not
      Vote)

  `income`
      an integer vector ranging from "4" (Less than \\$5000) to "17"
      (Greater than \\$75000) denoting family income. See the CPS codebook
      for more information on variable coding

  `education`
      an integer vector ranging from "1" (Less than High School Education)
      to "4" (More than a College Education). See the CPS codebook for
      more information on variable coding

  `age`
      an integer vector ranging from "18" to "85"

  `female`
      an integer vector taking on values "1" (Female) and "0" (Male)

  Census Bureau Current Population Survey

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `voteincome.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1500 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'voteincome.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/voteincome.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='voteincome.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
