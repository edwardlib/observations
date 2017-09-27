# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aus_election_polling(path):
  """Political opinion polls in Australia, 2004-07

  The results of 239 published opinion polls measuring vote intentions
  (1st preference vote intention in a House of Representatives election)
  between the 2004 and 2007 Australian Federal elections, from 4 survey
  houses.

  A data frame with 239 observations on the following 14 variables.

  `ALP`
      a numeric vector, percentage of respondents reported as intending to
      vote for the Australian Labor Party

  `Lib`
      a numeric vector, percentage of respondents reported as intending to
      vote for the Liberal Party

  `Nat`
      a numeric vector, percentage of respondents reported as intending to
      vote for the National Party

  `Green`
      a numeric vector, percentage of respondents reported as intending to
      vote for the Greens

  `FamilyFirst`
      a numeric vector, percentage of respondents reported as intending to
      vote for the Family First party

  `Dems`
      a numeric vector, percentage of respondents reported as intending to
      vote for the Australian Democrats

  `OneNation`
      a numeric vector, percentage of respondents reported as intending to
      vote for One Nation

  `DK`
      a numeric vector, percentage of respondents reported as expressing
      no preference or a “don't know” response

  `sampleSize`
      a numeric vector, reported sample size of the poll

  `org`
      a factor with levels `Galaxy`, `Morgan, F2F`, `Newspoll`,
      `Nielsen` and `Morgan, Phone`, indicating the survey house
      and/or mode of the poll

  `startDate`
      a Date, reported start of the field period

  `endDate`
      a Date, reported end of the field period

  `source`
      a character vector, source of the poll report

  `remark`
      a character vector, remarks noted by author and/or research
      assistant coders

  See the `source` variable. Andrea Abel assisted with the data
  collection.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aus_election_polling.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 239 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aus_election_polling.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/AustralianElectionPolling.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aus_election_polling.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
