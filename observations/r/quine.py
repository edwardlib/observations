# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def quine(path):
  """Absenteeism from School in Rural New South Wales

  The `quine` data frame has 146 rows and 5 columns. Children from
  Walgett, New South Wales, Australia, were classified by Culture, Age,
  Sex and Learner status and the number of days absent from school in a
  particular school year was recorded.

  This data frame contains the following columns:

  `Eth`
      ethnic background: Aboriginal or Not, (`"A"` or `"N"`).

  `Sex`
      sex: factor with levels (`"F"` or `"M"`).

  `Age`
      age group: Primary (`"F0"`), or forms `"F1,"` `"F2"` or
      `"F3"`.

  `Lrn`
      learner status: factor with levels Average or Slow learner,
      (`"AL"` or `"SL"`).

  `Days`
      days absent from school in the year.

  S. Quine, quoted in Aitkin, M. (1978) The analysis of unbalanced cross
  classifications (with discussion). *Journal of the Royal Statistical
  Society series A* **141**, 195–223.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `quine.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 146 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'quine.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/quine.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='quine.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
