# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vote92(path):
  """Reports of voting in the 1992 U.S. Presidential election.

  Survey data containing self-reports of vote choice in the 1992 U.S.
  Presidential election, with numerous covariates, from the 1992 American
  National Election Studies.

  A data frame with 909 observations on the following 10 variables.

  `vote`
      a factor with levels `Perot` `Clinton` `Bush`

  `dem`
      a numeric vector, 1 if the respondent reports identifying with the
      Democratic party, 0 otherwise.

  `rep`
      a numeric vector, 1 if the respondent reports identifying with the
      Republican party, 0 otherwise

  `female`
      a numeric vector, 1 if the respondent is female, 0 otherwise

  `persfinance`
      a numeric vector, -1 if the respondent reports that their personal
      financial situation has gotten worse over the last 12 months, 0 for
      no change, 1 if better

  `natlecon`
      a numeric vector, -1 if the respondent reports that national
      economic conditions have gotten worse over the last 12 months, 0 for
      no change, 1 if better

  `clintondis`
      a numeric vector, squared difference between respondent's
      self-placement on a scale measure of political ideology and the
      respondent's placement of the Democratic candidate, Bill Clinton

  `bushdis`
      a numeric vector, squared ideological distance of the respondent
      from the Republican candidate, President George H.W. Bush

  `perotdis`
      a numeric vector, squared ideological distance of the respondent
      from the Reform Party candidate, Ross Perot

  Alvarez, R. Michael and Jonathan Nagler. 1995. Economics, issues and the
  Perot candidacy: Voter choice in the 1992 Presidential election.
  *American Journal of Political Science*. 39:714-44.

  Miller, Warren E., Donald R. Kinder, Steven J. Rosenstone and the
  National Election Studies. 1999. *National Election Studies, 1992:
  Pre-/Post-Election Study*. Center for Political Studies, University of
  Michigan: Ann Arbor, Michigan.

  Inter-University Consortium for Political and Social Research. Study
  Number 1112. http://dx.doi.org/10.3886/ICPSR01112.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vote92.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 909 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vote92.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/vote92.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vote92.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
