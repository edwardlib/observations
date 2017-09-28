# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nightingale(path):
  """Florence Nightingale's data on deaths from various causes in the Crimean W
  ar

  In the history of data visualization, Florence Nightingale is best
  remembered for her role as a social activist and her view that
  statistical data, presented in charts and diagrams, could be used as
  powerful arguments for medical reform.

  After witnessing deplorable sanitary conditions in the Crimea, she wrote
  several influential texts (Nightingale, 1858, 1859), including
  polar-area graphs (sometimes called "Coxcombs" or rose diagrams),
  showing the number of deaths in the Crimean from battle compared to
  disease or preventable causes that could be reduced by better
  battlefield nursing care.

  Her *Diagram of the Causes of Mortality in the Army in the East* showed
  that most of the British soldiers who died during the Crimean War died
  of sickness rather than of wounds or other causes. It also showed that
  the death rate was higher in the first year of the war, before a
  Sanitary Commissioners arrived in March 1855 to improve hygiene in the
  camps and hospitals.

  A data frame with 24 observations on the following 10 variables.

  `Date`
      a Date, composed as
      `as.Date(paste(Year, Month, 1, sep='-'), "%Y-%b-%d")`

  `Month`
      Month of the Crimean War, an ordered factor

  `Year`
      Year of the Crimean War

  `Army`
      Estimated average monthly strength of the British army

  `Disease`
      Number of deaths from preventable or mitagable zymotic diseases

  `Wounds`
      Number of deaths directly from battle wounds

  `Other`
      Number of deaths from other causes

  `Disease.rate`
      Annual rate of deaths from preventable or mitagable zymotic
      diseases, per 1000

  `Wounds.rate`
      Annual rate of deaths directly from battle wounds, per 1000

  `Other.rate`
      Annual rate of deaths from other causes, per 1000

  The data were obtained from:

  Pearson, M. and Short, I. (2007). Understanding Uncertainty: Mathematics
  of the Coxcomb. http://understandinguncertainty.org/node/214.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nightingale.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nightingale.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Nightingale.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nightingale.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
