# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mofa(path):
  """International Expansion of U.S. Mofa's (majority–owned Foreign Affiliates)
  Expansion of U.S. Mofa's (majority–owned Foreign Affiliates) in
  Fire (finance, Insurance and Real Estate)

  a cross-section from 1982

  *number of observations* : 50

  *observation* : country

  *country* : United States

  A dataframe containing :

  capexp
      capital expenditures made by the MOFA's of nonbank U.S. corporations
      in finance, insurance and real estate. Source: "U.S. Direct
      Investment Abroad: 1982 Benchmark Survey data." Table III.C 6.

  gdp
      gross domestic product. Source: "World Bank, World Development
      Report 1984." Table 3. (This variable is scaled by a factor of
      1/100,000)

  sales
      sales made by the majority owned foreign affiliates of nonbank U.S.
      parents in finance, insurance and real estate. Source: "U.S. Direct
      Investment Abroad: 1982 Benchmark Survey Data." Table III.D 3. (This
      variable is scaled by a factor of 1/100)

  nbaf
      the number of U.S. affiliates in the host country. Source: "U.S.
      Direct Investment Abroad: 1982 Benchmark Survey Data." Table 5.
      (This variable is scaled by a factor of 1/100)

  netinc
      net income earned by MOFA's of nonbank U.S. corporations operating
      in the nonbanking financial sector of the host country. Source:
      "U.S. Direct Investment Abroad: 1982 Benchmark Survey Data." Table
      III.D 6.(This variable is scaled by a factor of 1/10)

  Ioannatos, Petros E. (1995) “Censored regression estimation under
  unobserved heterogeneity : a stochastic parameter approach”, *Journal of
  Business and Economics Statistics*, **13(3)**, july, 327–335.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mofa.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mofa.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Mofa.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mofa.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
