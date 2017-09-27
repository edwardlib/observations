# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nlschools(path):
  """Eighth-Grade Pupils in the Netherlands

  Snijders and Bosker (1999) use as a running example a study of 2287
  eighth-grade pupils (aged about 11) in 132 classes in 131 schools in the
  Netherlands. Only the variables used in our examples are supplied.

  This data frame contains 2287 rows and the following columns:

  `lang`
      language test score.

  `IQ`
      verbal IQ.

  `class`
      class ID.

  `GS`
      class size: number of eighth-grade pupils recorded in the class
      (there may be others: see `COMB`, and some may have been omitted
      with missing values).

  `SES`
      social-economic status of pupil's family.

  `COMB`
      were the pupils taught in a multi-grade class (`0/1`)? Classes
      which contained pupils from grades 7 and 8 are coded `1`, but only
      eighth-graders were tested.

  Snijders, T. A. B. and Bosker, R. J. (1999) *Multilevel Analysis. An
  Introduction to Basic and Advanced Multilevel Modelling.* London: Sage.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nlschools.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2287 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nlschools.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/nlschools.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nlschools.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
