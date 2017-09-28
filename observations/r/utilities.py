# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def utilities(path):
  """Utility bills

  Data from utility bills at a residence. `Utilities2` is a similar data
  set with some additional variables.

  A data frame containing 117 observations for the following variables.

  -  `month` month (coded as a number)

  -  `day` day of month on which bill was calculated

  -  `year` year of bill

  -  `temp` average temperature (F) for billing period

  -  `kwh` electricity usage (kwh)

  -  `ccf` gas usage (ccf)

  -  `thermsPerDay` a numeric vector

  -  `billingDays` number of billing days in billing period

  -  `totalbill` total bill (in dollars)

  -  `gasbill` gas bill (in dollars)

  -  `elecbill` exectric bill (in dollars)

  -  `notes` notes about the billing period

  Daniel T. Kaplan, *Statistical modeling: A fresh approach*, 2009.

  See Also
  ~~~~~~~~

  `Utilities2`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `utilities.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 117 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'utilities.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Utilities.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='utilities.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
