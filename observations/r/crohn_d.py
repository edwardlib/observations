# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crohn_d(path):
  """Crohn's Disease Adverse Events Data

  Data set issued from a study of the adverse events of a drug on 117
  patients affected by Crohn's disease (a chronic inflammatory disease of
  the intestines).

  A data frame with 117 observations on the following 9 variables.

  `ID`
      the numeric patient IDs

  `nrAdvE`
      the number of adverse events

  `BMI`
      Body MASS Index, i.e., *weight[kg] / (height[m])^2*.

  `height`
      in cm

  `country`
      a factor with levels `0` and `1`

  `sex`
      the person's gender, a binary factor with levels `M` `F`

  `age`
      in years, a numeric vector

  `weight`
      in kilograms, a numeric vector

  `treat`
      how CD was treated: a factor with levels `0`, `1` and `2`,
      meaning placebo, drug 1 and drug 2.

  form the authors of the reference, with permission by the original data
  collecting agency.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crohn_d.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 117 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crohn_d.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/CrohnD.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crohn_d.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
