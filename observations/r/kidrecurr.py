# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kidrecurr(path):
  """Data on 38 individuals using a kidney dialysis machine

  Data on 38 individuals using a kidney dialysis machine See Problem
  13.5.2

  A data frame with 38 observations on the following 10 variables.

  patient
      Patient number

  time1
      Time one of recurrence of infection, days

  infect1
      Indicator infection one (1=yes, 0=no)

  time2
      Time two of recurrence of infection, days

  infect2
      Indicator infection two (1=yes, 0=no)

  age
      Patient's age

  gender
      Patient's gender

  gn
      Disease type GN (1=yes, 0=no)

  an
      Disease type AN (1=yes, 0=no)

  pkd
      Disease type PKD (1=yes, 0=no)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. McGilchrist and Aisbett 47
  (1991):461-466.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kidrecurr.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kidrecurr.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/kidrecurr.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kidrecurr.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
