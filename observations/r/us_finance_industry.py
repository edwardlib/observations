# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_finance_industry(path):
  """US Finance Industry Profits

  A `data.frame` giving the profits of the finance industry in the
  United States as a proportion of total corporate domestic profits.

  A `data.frame` with the following columns:

  year
      integer year starting with 1929

  CorporateProfitsAdj
      Corporate profits with inventory valuation and capital consumption
      adjustments in billions of current (not adjusted for inflation) US
      dollars

  Domestic
      Domestic industries profits in billions

  Financial
      Financial industries profits in billions

  Nonfinancial
      Nonfinancial industries profits in billions

  restOfWorld
      Profits of the "Rest of the world" in their contribution to US Gross
      Domestic Product in billions

  FinanceProportion
      = Financial/Domestic

  http://www.bea.gov: Under "U.S. Economic Accounts", first select
  "Corporate Profits" under "National". Then next to "Interactive Tables",
  select, "National Income and Product Accounts Tables". From there,
  select "Begin using the data...". Under "Section 6 - income and
  employment by industry", select each of the tables starting "Table
  6.16". As of February 2013, there were 4 such tables available: Table
  6.16A, 6.16B, 6.16C and 6.16D. Each of the last three are available in
  annual and quarterly summaries. The `USFinanceIndustry` data combined
  the first 4 rows of the 4 annual summary tables.

  See Also
  ~~~~~~~~

  `readNIPA`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_finance_industry.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 84 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_finance_industry.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/USFinanceIndustry.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_finance_industry.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
