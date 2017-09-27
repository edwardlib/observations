# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ams_survey(path):
  """American Math Society Survey Data

  Counts of new PhDs in the mathematical sciences for 2008-09 and 2011-12
  categorized by type of institution, gender, and US citizenship status.

  A data frame with 24 observations on the following 5 variables.

  type
      a factor with levels `I(Pu)` for group I public universities,
      `I(Pr)` for group I private universities, `II` and `III` for
      groups II and III, `IV` for statistics and biostatistics programs,
      and `Va` for applied mathemeatics programs.

  sex
      a factor with levels `Female`, `Male` of the recipient

  citizen
      a factor with levels `Non-US`, `US` giving citizenship status

  count
      The number of individuals of each type in 2008-09

  count11
      The number of individuals of each type in 2011-12

  http://www.ams.org/employment/surveyreports.html Supplementary Table 4
  in the 2008-09 data. See
  http://www.ams.org/profession/data/annual-survey/docsgrtd for more
  recent data.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ams_survey.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ams_survey.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/AMSsurvey.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ams_survey.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
