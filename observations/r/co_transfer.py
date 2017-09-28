# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def co_transfer(path):
  """Carbon Monoxide Transfer

  The `co.transfer` data frame has 7 rows and 2 columns. Seven smokers
  with chickenpox had their levels of carbon monoxide transfer measured on
  entry to hospital and then again after 1 week. The main question being
  whether one week of hospitalization has changed the carbon monoxide
  transfer factor.

  This data frame contains the following columns:

  `entry`
      Carbon monoxide transfer factor on entry to hospital.

  `week`
      Carbon monoxide transfer one week after admittance to hospital.

  The data were obtained from

  Hand, D.J., Daly, F., Lunn, A.D., McConway, K.J. and Ostrowski, E (1994)
  *A Handbook of Small Data Sets*. Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `co_transfer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'co_transfer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/co.transfer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='co_transfer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
