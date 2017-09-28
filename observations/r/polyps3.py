# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def polyps3(path):
  """Familial Andenomatous Polyposis

  Data from a placebo-controlled trial of a non-steroidal
  anti-inflammatory drug in the treatment of familial andenomatous
  polyposis (FAP).

  A data frame with 22 observations on the following 5 variables.

  `sex`
      a factor with levels `female` and `male`.

  `treatment`
      a factor with levels `placebo` and `active`.

  `baseline`
      the baseline number of polyps.

  `age`
      the age of the patient.

  `number3m`
      the number of polyps after three month.

  F. M. Giardiello, S. R. Hamilton, A. J. Krush, S. Piantadosi, L. M.
  Hylind, P. Celano, S. V. Booker, C. R. Robinson and G. J. A. Offerhaus
  (1993), Treatment of colonic and rectal adenomas with sulindac in
  familial adenomatous polyposis. *New England Journal of Medicine*,
  **328**\ (18), 1313–1316.

  S. Piantadosi (1997), *Clinical Trials: A Methodologic Perspective*.
  John Wiley \\& Sons, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `polyps3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'polyps3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/polyps3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='polyps3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
