# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def political_info(path):
  """Interviewer ratings of respondent levels of political information

  Interviewers administering the 2000 American National Election Studies
  assigned an ordinal rating to each respondent's "general level of
  information" about politics and public affairs.

  A data frame with 1807 observations on the following 8 variables.

  `y`
      interviewer rating, a factor with levels `Very Low` `Fairly Low`
      `Average` `Fairly High` `Very High`

  `collegeDegree`
      a factor with levels `No` `Yes`

  `female`
      a factor with levels `No` `Yes`

  `age`
      a numeric vector, respondent age in years

  `homeOwn`
      a factor with levels `No` `Yes`

  `govt`
      a factor with levels `No` `Yes`

  `length`
      a numeric vector, length of ANES pre-election interview in minutes

  `id`
      a factor, unique identifier for each interviewer

  The National Election Studies (www.electionstudies.org). THE 2000
  NATIONAL ELECTION STUDY [dataset]. Ann Arbor, MI: University of
  Michigan, Center for Political Studies [producer and distributor].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `political_info.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1807 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'political_info.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/politicalInformation.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='political_info.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
