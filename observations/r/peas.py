# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def peas(path):
  """Galton's Peas

  Francis Galton introduced the correlation coefficient with an analysis
  of the similarities of the parent and child generation of 700 sweet
  peas.

  A data frame with 700 observations on the following 2 variables.

  `parent`
      The mean diameter of the mother pea for 700 peas

  `child`
      The mean diameter of the daughter pea for 700 sweet peas

  Stanton, Jeffrey M. (2001) Galton, Pearson, and the Peas: A brief
  history of linear regression for statistics intstructors, Journal of
  Statistics Education, 9. (retrieved from the web from
  http://www.amstat.org/publications/jse/v9n3/stanton.html) reproduces the
  table from Galton, 1894, Table 2.

  The data were generated from this table.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `peas.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 700 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'peas.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/peas.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='peas.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
