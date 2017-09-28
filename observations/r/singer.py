# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def singer(path):
  """Heights of New York Choral Society singers

  Heights in inches of the singers in the New York Choral Society in 1979.
  The data are grouped according to voice part. The vocal range for each
  voice part increases in pitch according to the following order: Bass 2,
  Bass 1, Tenor 2, Tenor 1, Alto 2, Alto 1, Soprano 2, Soprano 1.

  A data frame with 235 observations on the following 2 variables.

  height
      Height in inches of the singers.

  voice.part
      (Unordered) factor with levels "`Bass 2`", "`Bass 1`",
      "`Tenor 2`", "`Tenor 1`", "`Alto 2`", "`Alto 1`",
      "`Soprano 2`", "`Soprano 1`".

  Author(s)
  ~~~~~~~~~

  Documentation contributed by Kevin Wright.

  Chambers, J.M., W. S. Cleveland, B. Kleiner, and P. A. Tukey. (1983).
  *Graphical Methods for Data Analysis*. Chapman and Hall, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `singer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 235 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'singer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lattice/singer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='singer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
