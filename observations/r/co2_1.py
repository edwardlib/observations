# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def co2_1(path):
  """Mauna Loa Atmospheric CO2 Concentration

  Atmospheric concentrations of CO\ *2* are expressed in parts per million
  (ppm) and reported in the preliminary 1997 SIO manometric mole fraction
  scale.

  A time series of 468 observations; monthly from 1959 to 1997.

  Keeling, C. D. and Whorf, T. P., Scripps Institution of Oceanography
  (SIO), University of California, La Jolla, California USA 92093-0220.

  ftp://cdiac.esd.ornl.gov/pub/maunaloa-co2/maunaloa.co2.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `co2_1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 468 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'co2_1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/co2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='co2_1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
