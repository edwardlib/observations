# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def swiss(path):
  """Swiss Fertility and Socioeconomic Indicators (1888) Data

  Standardized fertility measure and socio-economic indicators for each of
  47 French-speaking provinces of Switzerland at about 1888.

  A data frame with 47 observations on 6 variables, *each* of which is in
  percent, i.e., in *[0, 100]*.

  +------+-----------------+-------------------------------------------------+
  | [,1] | Fertility       | *Ig*, ‘common standardized fertility measure’   |
  +------+-----------------+-------------------------------------------------+
  | [,2] | Agriculture     | % of males involved in agriculture as occupation|
  +------+-----------------+-------------------------------------------------+
  | [,3] | Examination     | % draftees receiving highest mark on army       |
  |      |                 | examination                                     |
  +------+-----------------+-------------------------------------------------+
  | [,4] | Education       | % education beyond primary school for draftees. |
  +------+-----------------+-------------------------------------------------+
  | [,5] | Catholic        | % ‘catholic’ (as opposed to ‘protestant’).      |
  +------+-----------------+-------------------------------------------------+
  | [,6] | Infant.Mortality| live births who live less than 1 year.          |
  +------+-----------------+-------------------------------------------------+

  All variables but ‘Fertility’ give proportions of the population.

  Details
  ~~~~~~~

  (paraphrasing Mosteller and Tukey):

  Switzerland, in 1888, was entering a period known as the *demographic
  transition*; i.e., its fertility was beginning to fall from the high
  level typical of underdeveloped countries.

  The data collected are for 47 French-speaking “provinces” at about 1888.

  Here, all variables are scaled to *[0, 100]*, where in the original, all
  but `"Catholic"` were scaled to *[0, 1]*.

  Project “16P5”, pages 549–551 in

  Mosteller, F. and Tukey, J. W. (1977) *Data Analysis and Regression: A
  Second Course in Statistics*. Addison-Wesley, Reading Mass.

  indicating their source as “Data used by permission of Franice van de
  Walle. Office of Population Research, Princeton University, 1976.
  Unpublished data assembled under NICHD contract number No 1-HD-O-2077.”

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `swiss.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 47 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'swiss.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/swiss.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='swiss.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
