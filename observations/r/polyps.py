# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def polyps(path):
  """Familial Andenomatous Polyposis

  Data from a placebo-controlled trial of a non-steroidal
  anti-inflammatory drug in the treatment of familial andenomatous
  polyposis (FAP).

  A data frame with 20 observations on the following 3 variables.

  `number`
      number of colonic polyps at 12 months.

  `treat`
      treatment arms of the trail, a factor with levels `placebo` and
      `drug`.

  `age`
      the age of the patient.

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
      Filename is `polyps.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'polyps.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/polyps.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='polyps.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
