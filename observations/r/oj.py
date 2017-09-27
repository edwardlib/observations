# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def oj(path):
  """Orange Juice Data

  The data contains 1070 purchases where the customer either purchased
  Citrus Hill or Minute Maid Orange Juice. A number of characteristics of
  the customer and product are recorded.

  A data frame with 1070 observations on the following 18 variables.

  `Purchase`
      A factor with levels `CH` and `MM` indicating whether the
      customer purchased Citrus Hill or Minute Maid Orange Juice

  `WeekofPurchase`
      Week of purchase

  `StoreID`
      Store ID

  `PriceCH`
      Price charged for CH

  `PriceMM`
      Price charged for MM

  `DiscCH`
      Discount offered for CH

  `DiscMM`
      Discount offered for MM

  `SpecialCH`
      Indicator of special on CH

  `SpecialMM`
      Indicator of special on MM

  `LoyalCH`
      Customer brand loyalty for CH

  `SalePriceMM`
      Sale price for MM

  `SalePriceCH`
      Sale price for CH

  `PriceDiff`
      Sale price of MM less sale price of CH

  `Store7`
      A factor with levels `No` and `Yes` indicating whether the sale
      is at Store 7

  `PctDiscMM`
      Percentage discount for MM

  `PctDiscCH`
      Percentage discount for CH

  `ListPriceDiff`
      List price of MM less list price of CH

  `STORE`
      Which of 5 possible stores the sale occured at

  Stine, Robert A., Foster, Dean P., Waterman, Richard P. Business
  Analysis Using Regression (1998). Published by Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `oj.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1070 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'oj.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/OJ.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='oj.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
