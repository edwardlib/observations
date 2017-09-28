# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def political(path):
  """Political

  Survey of political activity for Grinnell College students

  A dataset with 59 observations on the following 9 variables.

  `Year`

  Class year (1 to 4)

  `Sex`

  `0`\ =male or `1`\ =female

  `Vote`

  Voting status: `0`\ =not eligible, `1`\ =eligible/not registered,
  `2`\ =registered/didn't vote, `4`\ =voted

  `Paper`

  Read news (per week): `0`\ =never, code1=less than once, `2`\ =once,
  `3`\ =2 or 3 times, `4`\ =daily

  `Edit`

  Read editorial page? `0`\ =no or `1`\ =yes

  `TV`

  Watch TV news: `0`\ =never, code1=less than once, `2`\ =once,
  `3`\ =2 or 3 times, `4`\ =daily

  `Ethics`

  Politics should be ruled by: `1`\ =ethical considerations to
  `5`\ =practical power

  `Inform`

  How informed are you about politics? `1`\ =uninformed to `5`\ =very
  well informed

  `Participate`

  Missing if Vote=0, `0` if Vote=1 or 2, `1` if Vote=3


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `political.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 59 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'political.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Political.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='political.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
