# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def adler(path):
  """Experimenter Expectations

  The `Adler` data frame has 97 rows and 3 columns.

  The “experimenters” were the actual subjects of the study. They
  collected ratings of the apparent successfulness of people in pictures
  who were pre-selected for their average appearance. The experimenters
  were told prior to collecting data that the pictures were either high or
  low in their appearance of success, and were instructed to get good
  data, scientific data, or were given no such instruction. Each
  experimenter collected ratings from 18 randomly assigned respondents; a
  few subjects were deleted at random to produce an unbalanced design.

  This data frame contains the following columns:

  instruction
      a factor with levels: `GOOD`, good data; `NONE`, no stress;
      `SCIENTIFIC`, scientific data.

  expectation
      a factor with levels: `HIGH`, expect high ratings; `LOW`, expect
      low ratings.

  rating
      The average rating obtained.

  Adler, N. E. (1973) Impact of prior sets given experimenters and
  subjects on the experimenter expectancy effect. *Sociometry* **36**,
  113–126.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `adler.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 97 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'adler.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Adler.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='adler.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
