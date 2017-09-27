# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def birthwt(path):
  """Risk Factors Associated with Low Infant Birth Weight

  The `birthwt` data frame has 189 rows and 10 columns. The data were
  collected at Baystate Medical Center, Springfield, Mass during 1986.

  This data frame contains the following columns:

  `low`
      indicator of birth weight less than 2.5 kg.

  `age`
      mother's age in years.

  `lwt`
      mother's weight in pounds at last menstrual period.

  `race`
      mother's race (`1` = white, `2` = black, `3` = other).

  `smoke`
      smoking status during pregnancy.

  `ptl`
      number of previous premature labours.

  `ht`
      history of hypertension.

  `ui`
      presence of uterine irritability.

  `ftv`
      number of physician visits during the first trimester.

  `bwt`
      birth weight in grams.

  Hosmer, D.W. and Lemeshow, S. (1989) *Applied Logistic Regression.* New
  York: Wiley

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `birthwt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 189 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'birthwt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/birthwt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='birthwt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
