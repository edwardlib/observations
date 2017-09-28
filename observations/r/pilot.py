# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pilot(path):
  """Pilot-Plant Data

  Pilot-Plant data from Daniel and Wood (1971). The response variable
  corresponds to the acid content determined by titration and the
  explanatory variable is the organic acid content determined by
  extraction and weighing. This data set was analyzed also by Yale and
  Forsythe (1976).

  A data frame with 20 observations on the following 2 variables.

  `X`
      Organic acid content - extraction

  `Y`
      Acid content - titration

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, page 21, table 1.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pilot.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pilot.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/pilot.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pilot.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
