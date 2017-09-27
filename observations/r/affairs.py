# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def affairs(path):
  """affairs

  Data from Fair (1978). Although Fair used a tobit model with the data,
  the outcome measure can be modeled as a count. In fact, Greene (2003)
  modeled it as Poisson, but given the amount of overdispersion in the
  data, employing a negative binomial model is an appropriate strategy.
  The data is stored in the affairs data set. Naffairs is the response
  variable, indicating the number of affairs reported by the participant
  in the past year.

  A data frame with 601 observations on the following 18 variables.

  `naffairs`
      number of affairs within last year

  `kids`
      1=have children;0= no children

  `vryunhap`
      (1/0) very unhappily married

  `unhap`
      (1/0) unhappily married

  `avgmarr`
      (1/0) average married

  `hapavg`
      (1/0) happily married

  `vryhap`
      (1/0) very happily married

  `antirel`
      (1/0) anti religious

  `notrel`
      (1/0) not religious

  `slghtrel`
      (1/0) slightly religious

  `smerel`
      (1/0) somewhat religious

  `vryrel`
      (1/0) very religious

  `yrsmarr1`
      (1/0) >0.75 yrs

  `yrsmarr2`
      (1/0) >1.5 yrs

  `yrsmarr3`
      (1/0) >4.0 yrs

  `yrsmarr4`
      (1/0) >7.0 yrs

  `yrsmarr5`
      (1/0) >10.0 yrs

  `yrsmarr6`
      (1/0) >15.0 yrs

  Fair, R. (1978). A Theory of Extramarital Affairs, Journal of Political
  Economy, 86: 45-61. Greene, W.H. (2003). Econometric Analysis, Fifth
  Edition, New York: Macmillan.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `affairs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 601 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'affairs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/affairs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='affairs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
