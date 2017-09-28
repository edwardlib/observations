# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def insurance_vote(path):
  """InsuranceVote

  Congressional votes

  A dataset with 435 observations on the following 9 variables.

  `Party`

  Party affilication: `D`\ =Democrat or `R`\ =Republican

  `Dist.`

  Congressional district (State-Number)

  `InsVote`

  Vote on the health insurance bill: `1`\ =yes or `0`\ =no

  `Rep`

  Indicator for Republicans

  `Dem`

  Indicator for Democrats

  `Private`

  Percentage of non-senior citizens in district with private health
  insurance

  `Public`

  Percentage of non-senior citizens in district with public health
  insurance

  `Uninsured`

  Percentage of non-senior citizens in district with no health insurance

  `Obama`

  District winner in 2008 presidential election: `1`\ =Obama
  `0`\ =McCain

  Insurance data are from the American Community Survey
  (http://www.census.gov/acs/www/data\_documentation/data\_main/). Roll
  call of congressional votes on this bill can be found at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `insurance_vote.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 435 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'insurance_vote.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/InsuranceVote.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='insurance_vote.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
