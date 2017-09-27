# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pastes(path):
  """Paste strength by batch and cask

  Strength of a chemical paste product; its quality depending on the
  delivery batch, and the cask within the delivery.

  A data frame with 60 observations on the following 4 variables.

  `strength`
      paste strength.

  `batch`
      delivery batch from which the sample was sample. A factor with 10
      levels: ‘A’ to ‘J’.

  `cask`
      cask within the delivery batch from which the sample was chosen. A
      factor with 3 levels: ‘a’ to ‘c’.

  `sample`
      the sample of paste whose strength was assayed, two assays per
      sample. A factor with 30 levels: ‘A:a’ to ‘J:c’.

  O.L. Davies and P.L. Goldsmith (eds), *Statistical Methods in Research
  and Production, 4th ed.*, Oliver and Boyd, (1972), section 6.5

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pastes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pastes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/Pastes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pastes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
