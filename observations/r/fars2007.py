# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fars2007(path):
  """US fatal road accident data, 2007 and 2008

  Data are included on variables that may be relevant to assessing airbag
  and seatbelt effectiveness in preventing fatal injury.

  A data frame with 72548 observations on the following 24 variables.

  `Obs.`
      a numeric vector

  `state`
      a numeric vector

  `casenum`
      a numeric vector

  `vnum`
      a numeric vector

  `pnum`
      a numeric vector

  `lightcond`
      a numeric vector

  `numfatal`
      a numeric vector

  `vforms`
      a numeric vector

  `age`
      a numeric vector

  `airbag`
      a numeric vector

  `injury`
      a numeric vector

  `ptype`
      a numeric vector

  `restraint`
      a numeric vector

  `seatpos`
      a numeric vector

  `sex`
      a numeric vector

  `body`
      a numeric vector

  `inimpact`
      a numeric vector

  `mhevent`
      a numeric vector

  `vfatcount`
      a numeric vector

  `numoccs`
      a numeric vector

  `travspd`
      a numeric vector

  `make`
      a numeric vector

  `model`
      a numeric vector

  `modelyr`
      a numeric vector

  http://www-fars.nhtsa.dot.gov/Main/index.aspx

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fars2007.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72548 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fars2007.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gamclass/fars2007.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fars2007.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
