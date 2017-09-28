# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def absentee(path):
  """Absentee and Machine Ballots in Pennsylvania State Senate Races

  Absentee ballot outcomes contrasted with machine ballots, cast in
  Pennsylvania State Senate elections, selected districts, 1982-1993.

  A data frame with 22 observations on the following 8 variables.

  `year`
      a numeric vector, year of election, 19xx

  `district`
      a numeric vector, Pennsylvania State Senate district

  `absdem`
      a numeric vector, absentee ballots cast for the Democratic candidate

  `absrep`
      a numeric vector, absentee ballots cast for the Republican candidate

  `machdem`
      a numeric vector, votes cast on voting machines for the Democratic
      candidate

  `machrep`
      a numeric vector, votes cast on voting machines for the Republican
      candidate

  `dabs`
      a numeric vector, Democratic margin among absentee ballots

  `dmach`
      a numeric vector, Democratic margin among ballots case on voting
      machines

  Ashenfelter, Orley. 1994. Report on Expected Asbentee Ballots.
  Typescript. Department of Economics, Princeton University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `absentee.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'absentee.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/absentee.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='absentee.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
