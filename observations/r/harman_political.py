# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def harman_political(path):
  """Eight political variables used by Harman (1967) as example 8.17

  Another one of the many Harman (1967) data sets. This contains 8
  political variables taken over 147 election areas. The principal factor
  method with SMCs as communalities match those of table 8.18. The data
  are used by Dziubian and Shirkey as an example of the Kaiser-Meyer-Olkin
  test of factor adequacy.

  The format is: num [1:8, 1:8] 1 0.84 0.62 -0.53 0.03 0.57 -0.33 -0.63
  0.84 1 ... - attr(\*, "dimnames")=List of 2 ..$ : chr [1:8] "Lewis"
  "Roosevelt" "Party Voting" "Median Rental" ... ..$ : chr [1:8] "Lewis"
  "Roosevelt" "Party Voting" "Median Rental" ...

  Harman, Harry Horace (1976) Modern factor analysis, 3d ed., rev,
  University of Chicago Press. Chicago. p 166.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `harman_political.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'harman_political.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Harman.political.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='harman_political.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
