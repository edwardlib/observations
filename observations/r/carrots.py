# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def carrots(path):
  """Insect Damages on Carrots

  The damage carrots data set from Phelps (1982) was used by McCullagh and
  Nelder (1989) in order to illustrate diagnostic techniques because of
  the presence of an outlier. In a soil experiment trial with three
  blocks, eight levels of insecticide were applied and the carrots were
  tested for insect damage.

  A data frame with 24 observations on the following 4 variables.

  success
      integer giving the number of carrots with insect damage.

  total
      integer giving the total number of carrots per experimental unit.

  logdose
      a numeric vector giving log(dose) values (eight different levels
      only).

  block
      factor with levels `B1` to `B3`

  | Phelps, K. (1982). Use of the complementary log-log function to
    describe doseresponse relationships in insecticide evaluation field
    trials.
  | In R. Gilchrist (Ed.), *Lecture Notes in Statistics, No. 14. GLIM.82:
    Proceedings of the International Conference on Generalized Linear
    Models*; Springer-Verlag.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `carrots.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'carrots.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/carrots.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='carrots.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
