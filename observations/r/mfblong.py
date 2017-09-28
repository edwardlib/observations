# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mfblong(path):
  """Example data for ACEnucfam

  This is the companion data for ACEnucfam.

  The data is a random subset of the birth weight data from the mental
  health registry of Norway.

  male-a dummy variable for being male; first-a dummy variable for being
  the first child; midage-a dummy variable for mother aged 20-35 at time
  of birth; highage-a dummy variable for mother older than 35 at time of
  birth and birthyr-year of birth minus 1967 (earliest birth year in birth
  registry).

  The data were obtained from the Biometrics website and preprocessed with
  f.mfb.R.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mfblong.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3000 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mfblong.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/mfblong.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mfblong.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
