# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dactyl(path):
  """Edgeworth's counts of dactyls in Virgil's Aeneid

  Edgeworth (1885) took the first 75 lines in Book XI of Virgil's *Aeneid*
  and classified each of the first four "feet" of the line as a dactyl
  (one long syllable followed by two short ones) or not.

  Grouping the lines in blocks of five gave a 4 x 25 table of counts,
  represented here as a data frame with ordered factors, `Foot` and
  `Lines`. Edgeworth used this table in what was among the first
  examples of analysis of variance applied to a two-way classification.

  A data frame with 60 observations on the following 3 variables.

  `Foot`
      an ordered factor with levels `1` < `2` < `3` < `4`

  `Lines`
      an ordered factor with levels `1:5` < `6:10` < `11:15` <
      `16:20` < `21:25` < `26:30` < `31:35` < `36:40` <
      `41:45` < `46:50` < `51:55` < `56:60` < `61:65` <
      `66:70` < `71:75`

  `count`
      number of dactyls

  Stigler, S. (1999) *Statistics on the Table* Cambridge, MA: Harvard
  University Press, table 5.1.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dactyl.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dactyl.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Dactyl.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dactyl.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
