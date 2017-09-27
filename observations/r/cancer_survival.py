# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cancer_survival(path):
  """CancerSurvival

  Cancer survival with ascorbate supplement

  A dataset with 64 observations on the following 2 variables.

  `Survival`

  Survival time (in days)

  `Organ`

  `Breast`, `Bronchus`, `Colon`, `Ovary`, or `Stomach`

  From the article "Supplemental Ascorbate in the Supportive Treatment of
  Cancer: Reevaluation of Prolongation of Survival Times in Terminal Human
  Cancer" by Ewan Cameron and Linus Pauling, Proceedings of the National
  Academy of Sciences of the United States of America, Vol. 75, No. 9

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cancer_survival.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 64 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cancer_survival.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/CancerSurvival.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cancer_survival.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
