# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def metabolic_rate(path):
  """Metabolic Rate of Caterpillars

  Body size and metabolic rate of Manduca Sexta caterpillars

  A dataset with 305 observations on the following 7 variables.

  `Computer`

  ID number of the computer used to measure metabolic rate

  `BodySize`

  Size of the caterpillar (in grams)

  `LogBodySize`

  Log (base 10) of BodySize

  `Instar`

  Number from 1 (smallest) to 5 (largest) indicating stage of the
  caterpillar's life

  `CO2ppm`

  Carbon dioxide concentration (in ppm)

  `Mrate`

  Metabolic rate

  `LogMrate`

  Log (base 10) of metablic rate

  We thank Professor Itagaki and his research students for sharing these

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `metabolic_rate.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 305 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'metabolic_rate.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MetabolicRate.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='metabolic_rate.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
