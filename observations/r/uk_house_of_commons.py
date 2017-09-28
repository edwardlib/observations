# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def uk_house_of_commons(path):
  """1992 United Kingdom electoral returns

  Electoral returns, selected constituencies, 1992 general election for
  the British House of Commons

  A data frame with 521 observations on the following 12 variables.

  `constituency`
      a character vector, name of the House of Commons constituency

  `county`
      a character vector, county of the House of Commons constituency

  `y1`
      a numeric vector, log-odds of Conservative to LibDem vote share

  `y2`
      a numeric vector, log-odds of Labor to LibDem vote share

  `y1lag`
      a numeric vector, `y1` from previous election

  `y2lag`
      a numeric vector, `y2` from previous election

  `coninc`
      a numeric vector, 1 if the incumbent is a Conservative, 0 otherwise

  `labinc`
      a numeric vector, 1 if the incumbent is from the Labor Party, 0
      otherwise

  `libinc`
      a numeric vector, 1 if the incumbent is from the LibDems, 0
      otherwise

  `v1`
      a numeric vector, Conservative vote share (proportion of 3 party
      vote)

  `v2`
      a numeric vector, Labor vote share (proportion of 3 party vote)

  `v3`
      a numeric vector, LibDem vote share (proportion of 3 party vote)

  Jonathan Katz; Gary King. 1999. "Replication data for: A Statistical
  Model of Multiparty Electoral Data",
  http://hdl.handle.net/1902.1/QIGTWZYTLZ

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `uk_house_of_commons.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 521 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'uk_house_of_commons.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/UKHouseOfCommons.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='uk_house_of_commons.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
