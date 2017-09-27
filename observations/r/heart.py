# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def heart(path):
  """Heart Catherization Data

  This data set was analyzed by Weisberg (1980) and Chambers et al.
  (1983). A catheter is passed into a major vein or artery at the femoral
  region and moved into the heart. The proper length of the introduced
  catheter has to be guessed by the physician. The aim of the data set is
  to describe the relation between the catheter length and the patient's
  height (X1) and weight (X2).

  This data sets is used to demonstrate the effects caused by
  collinearity. The correlation between height and weight is so high that
  either variable almost completely determines the other.

  A data frame with 12 observations on the following 3 variables.

  `height`
      Patient's height in inches

  `weight`
      Patient's weights in pounds

  `clength`
      Y: Catheter Length (in centimeters)

  Weisberg (1980)

  Chambers et al. (1983)

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.103, table 13.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `heart.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 172 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'heart.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/heart.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='heart.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
