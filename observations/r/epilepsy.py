# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def epilepsy(path):
  """Epilepsy Attacks Data Set

  Data from a clinical trial of 59 patients with epilepsy (Breslow, 1996)
  in order to illustrate diagnostic techniques in Poisson regression.

  A data frame with 59 observations on the following 11 variables.

  `ID`
      Patient identification number

  `Y1`
      Number of epilepsy attacks patients have during the first follow-up
      period

  `Y2`
      Number of epilepsy attacks patients have during the second follow-up
      period

  `Y3`
      Number of epilepsy attacks patients have during the third follow-up
      period

  `Y4`
      Number of epilepsy attacks patients have during the forth follow-up
      period

  `Base`
      Number of epileptic attacks recorded during 8 week period prior to
      randomization

  `Age`
      Age of the patients

  `Trt`
      a factor with levels `placebo` `progabide` indicating whether
      the anti-epilepsy drug Progabide has been applied or not

  `Ysum`
      Total number of epilepsy attacks patients have during the four
      follow-up periods

  `Age10`
      Age of the patients devided by 10

  `Base4`
      Variable `Base` devided by 4

  Thall, P.F. and Vail S.C. (1990) Some covariance models for longitudinal
  count data with overdispersion. *Biometrics* **46**, 657–671.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `epilepsy.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 236 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'epilepsy.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/epilepsy.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='epilepsy.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
