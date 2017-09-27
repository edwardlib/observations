# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def edc_co2(path):
  """EPICA Dome C Ice Core 800KYr Carbon Dioxide Data

  Carbon dioxide record from the EPICA (European Project for Ice Coring in
  Antarctica) Dome C ice core covering 0 to 800 kyr BP.

  A data frame with 1096 observations on the following 2 variables.

  `age`
      Age in years before present (BP)

  `co2`
      CO2 level (ppmv)

http://www.ncdc.noaa.gov/paleo/icecore/antarctica/domec/domec_epica_data.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `edc_co2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1096 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'edc_co2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/edcCO2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='edc_co2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
