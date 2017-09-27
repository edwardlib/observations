# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def solder(path):
  """Soldering of Components on Printed-Circuit Boards

  The `solder` data frame has 720 rows and 6 columns, representing a
  balanced subset of a designed experiment varying 5 factors on the
  soldering of components on printed-circuit boards.

  This data frame contains the following columns:

  `Opening`
      a factor with levels L, M and S indicating the amount of clearance
      around the mounting pad.

  `Solder`
      a factor with levels Thick and Thin giving the thickness of the
      solder used.

  `Mask`
      a factor with levels A1.5, A3, B3 and B6 indicating the type and
      thickness of mask used.

  `PadType`
      a factor with levels D4, D6, D7, L4, L6, L7, L8, L9, W4 and W9
      giving the size and geometry of the mounting pad.

  `Panel`
      `1:3` indicating the panel on a board being tested.

  `skips`
      a numeric vector giving the number of visible solder skips.

  John M. Chambers and Trevor J. Hastie eds. (1992) *Statistical Models in
  S*, Wadsworth and Brooks/Cole, Pacific Grove, CA.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `solder.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 720 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'solder.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/rpart/solder.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='solder.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
