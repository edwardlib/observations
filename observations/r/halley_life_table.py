# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def halley_life_table(path):
  """Halley's Life Table

  In 1693 the famous English astronomer Edmond Halley studied the birth
  and death records of the city of Breslau, which had been transmitted to
  the Royal Society by Caspar Neumann. He produced a life table showing
  the number of people surviving to any age from a cohort born the same
  year. He also used his table to compute the price of life annuities.

  A data frame with 84 observations on the following 4 variables.

  `age`
      a numeric vector

  `deaths`
      number of deaths, *D\_k*, among people of age k, a numeric vector

  `number`
      size of the population, *P\_k* surviving until this age, a numeric
      vector

  `ratio`
      the ratio *P\_{k+1}/P\_k*, the conditional probability of surviving
      until age k + 1 given that one had already reached age k, a numeric
      vector

  N. Bacaer (2011), "Halley's life table (1693)", Ch 2, pp 5-10. In *A
  Short History of Mathematical Population Dynamics*, Springer-Verlag
  London, DOI 10.1007/978-0-85729-115-8\_2. Data taken from Table 1.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `halley_life_table.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 84 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'halley_life_table.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/HalleyLifeTable.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='halley_life_table.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
