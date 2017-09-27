# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def moore(path):
  """Status, Authoritarianism, and Conformity

  The `Moore` data frame has 45 rows and 4 columns. The data are for
  subjects in a social-psychological experiment, who were faced with
  manipulated disagreement from a partner of either of low or high status.
  The subjects could either conform to the partner's judgment or stick
  with their own judgment.

  This data frame contains the following columns:

  partner.status
      Partner's status. A factor with levels: `high`, `low`.

  conformity
      Number of conforming responses in 40 critical trials.

  fcategory
      F-Scale Categorized. A factor with levels (note levels out of
      order): `high`, `low`, `medium`.

  fscore
      Authoritarianism: F-Scale score.

  Moore, J. C., Jr. and Krupat, E. (1971) Relationship between source
  status, authoritarianism and conformity in a social setting.
  *Sociometry* **34**, 122–134.

  Personal communication from J. Moore, Department of Sociology, York
  University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `moore.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'moore.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Moore.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='moore.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
