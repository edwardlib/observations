# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def manaus(path):
  """Average Heights of the Rio Negro river at Manaus

  The `manaus` time series is of class `"ts"` and has 1080
  observations on one variable.

  The data values are monthly averages of the daily stages (heights) of
  the Rio Negro at Manaus. Manaus is 18km upstream from the confluence of
  the Rio Negro with the Amazon but because of the tiny slope of the water
  surface and the lower courses of its flatland affluents, they may be
  regarded as a good approximation of the water level in the Amazon at the
  confluence. The data here cover 90 years from January 1903 until
  December 1992.

  The Manaus gauge is tied in with an arbitrary bench mark of 100m set in
  the steps of the Municipal Prefecture; gauge readings are usually
  referred to sea level, on the basis of a mark on the steps leading to
  the Parish Church (Matriz), which is assumed to lie at an altitude of
  35.874 m according to observations made many years ago under the
  direction of Samuel Pereira, an engineer in charge of the Manaus
  Sanitation Committee Whereas such an altitude cannot, by any means, be
  considered to be a precise datum point, observations have been
  provisionally referred to it. The measurements are in metres.

  The data were kindly made available by Professors H. O'Reilly Sternberg
  and D. R. Brillinger of the University of California at Berkeley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `manaus.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1080 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'manaus.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/manaus.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='manaus.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
