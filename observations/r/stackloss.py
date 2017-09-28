# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def stackloss(path):
  """Brownlee's Stack Loss Plant Data

  Operational data of a plant for the oxidation of ammonia to nitric acid.

  `stackloss` is a data frame with 21 observations on 4 variables.

  [,1]

  `Air Flow`

  Flow of cooling air

  [,2]

  `Water Temp`

  Cooling Water Inlet Temperature

  [,3]

  `Acid Conc.`

  Concentration of acid [per 1000, minus 500]

  [,4]

  `stack.loss`

  Stack loss

  For compatibility with S-PLUS, the data sets `stack.x`, a matrix with
  the first three (independent) variables of the data frame, and
  `stack.loss`, the numeric vector giving the fourth (dependent)
  variable, are provided as well.

  Brownlee, K. A. (1960, 2nd ed. 1965) *Statistical Theory and Methodology
  in Science and Engineering*. New York: Wiley. pp. 491–500.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `stackloss.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'stackloss.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/stackloss.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='stackloss.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
