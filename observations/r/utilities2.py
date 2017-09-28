# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def utilities2(path):
  """Utility bills

  Data from utility bills at a private residence. This is an augmented
  version of `Utilities`.

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

  -  `ccfpday` average gas usage per day [`Utilities2` only]

  -  `kwhpday` average electric usage per day [`Utilities2` only]

  -  `gasbillpday` gas bill divided by billing days [`Utilities2`
     only]

  -  `elecbillpday` electric bill divided by billing days a numeric
     vector [`Utilities2` only]

  -  `totalbillpday` total bill divided by billing days a numeric vector
     [`Utilities2` only]

  -  `therms` `thermsPerDay * billingDays` [`Utilities2` only]

  -  `monthsSinceY2K` months since 2000 [`Utilities2` only]

  Daniel T. Kaplan, *Statistical modeling: A fresh approach*, 2009.

  See Also
  ~~~~~~~~

  `Utilities`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `utilities2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 117 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'utilities2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Utilities2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='utilities2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
