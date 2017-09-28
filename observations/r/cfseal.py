# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cfseal(path):
  """Cape Fur Seal Data

  The `cfseal` data frame has 30 rows and 11 columns consisting of
  weight measurements for various organs taken from 30 Cape Fur Seals that
  died as an unintended consequence of commercial fishing.

  This data frame contains the following columns:

  age
      a numeric vector

  weight
      a numeric vector

  heart
      a numeric vector

  lung
      a numeric vector

  liver
      a numeric vector

  spleen
      a numeric vector

  stomach
      a numeric vector

  leftkid
      a numeric vector

  rightkid
      a numeric vector

  kidney
      a numeric vector

  intestines
      a numeric vector

  Stewardson, C.L., Hemsley, S., Meyer, M.A., Canfield, P.J. and
  Maindonald, J.H. 1999. Gross and microscopic visceral anatomy of the
  male Cape fur seal, Arctocephalus pusillus pusillus (Pinnepedia:
  Otariidae), with reference to organ size and growth. Journal of Anatomy
  (Cambridge) 195: 235-255. (WWF project ZA-348)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cfseal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cfseal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/cfseal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cfseal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
