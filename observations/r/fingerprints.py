# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fingerprints(path):
  """Waite's data on Patterns in Fingerprints

  Waite (1915) was interested in analyzing the association of patterns in
  fingerprints, and produced a table of counts for 2000 right hands,
  classified by the number of fingers describable as a "whorl", a "small
  loop" (or neither). Because each hand contributes five fingers, the
  number of `Whorls + Loops` cannot exceed 5, so the contingency table
  is necessarily triangular.

  Karl Pearson (1904) introduced the test for independence in contingency
  tables, and by 1913 had developed methods for "restricted contingency
  tables," such as the triangular table analyzed by Waite. The general
  formulation of such tests for association in restricted tables is now
  referred to as models for quasi-independence.

  A frequency data frame with 36 observations on the following 3
  variables, representing a 6 x 6 table giving the cross-classification of
  the fingers on 2000 right hands as a whorl, small loop or neither.

  `Whorls`
      Number of whorls, an ordered factor with levels `0` < `1` <
      `2` < `3` < `4` < `5`

  `Loops`
      Number of small loops, an ordered factor with levels `0` < `1` <
      `2` < `3` < `4` < `5`

  `count`
      Number of hands

  Stigler, S. M. (1999). *Statistics on the Table*. Cambridge, MA: Harvard
  University Press, table 19.4.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fingerprints.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fingerprints.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Fingerprints.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fingerprints.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
