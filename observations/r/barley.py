# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def barley(path):
  """Yield data from a Minnesota barley trial

  Total yield in bushels per acre for 10 varieties at 6 sites in each of
  two years.

  A data frame with 120 observations on the following 4 variables.

  yield
      Yield (averaged across three blocks) in bushels/acre.

  variety
      Factor with levels `"Svansota"`, `"No. 462"`, `"Manchuria"`,
      `"No. 475"`, `"Velvet"`, `"Peatland"`, `"Glabron"`,
      `"No. 457"`, `"Wisconsin No. 38"`, `"Trebi"`.

  year
      Factor with levels `1932`, `1931`

  site
      Factor with 6 levels: `"Grand Rapids"`, `"Duluth"`,
      `"University Farm"`, `"Morris"`, `"Crookston"`, `"Waseca"`

  Immer, R. F., H. K. Hayes, and LeRoy Powers. (1934). Statistical
  Determination of Barley Varietal Adaptation. *Journal of the American
  Society of Agronomy*, **26**, 403–419.

  Wright, Kevin (2013). Revisiting Immer's Barley Data. *The American
  Statistician*, **67(3)**, 129–133.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `barley.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'barley.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lattice/barley.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='barley.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
