# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lbw(path):
  """lbw

  The data come to us from Hosmer and Lemeshow (2000). Called the low
  birth weight (lbw) data, the response is a binary variable, low, which
  indicates whether the birth weight of a baby is under 2500g (low=1), or
  over (low=0).

  A data frame with 189 observations on the following 10 variables.

  `low`
      1=low birthweight baby; 0=norml weight

  `smoke`
      1=history of mother smoking; 0=mother nonsmoker

  `race`
      categorical 1-3: 1=white; 2-=black; 3=other

  `age`
      age of mother: 14-45

  `lwt`
      weight (lbs) at last menstrual period: 80-250 lbs

  `ptl`
      number of false of premature labors: 0-3

  `ht`
      1=history of hypertension; 0 =no hypertension

  `ui`
      1=uterine irritability; 0 no irritability

  `ftv`
      number of physician visits in 1st trimester: 0-6

  `bwt`
      birth weight in grams: 709 - 4990 gr

  Hosmer, D and S. Lemeshow (2000), Applied Logistic Regression, Wiley

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lbw.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 189 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lbw.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/lbw.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lbw.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
