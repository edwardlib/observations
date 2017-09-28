# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cancer(path):
  """NCCTG Lung Cancer Data

  Survival in patients with advanced lung cancer from the North Central
  Cancer Treatment Group. Performance scores rate how well the patient can
  perform usual daily activities.

  inst:

  Institution code

  time:

  Survival time in days

  status:

  censoring status 1=censored, 2=dead

  age:

  Age in years

  sex:

  Male=1 Female=2

  ph.ecog:

  ECOG performance score (0=good 5=dead)

  ph.karno:

  Karnofsky performance score (bad=0-good=100) rated by physician

  pat.karno:

  Karnofsky performance score as rated by patient

  meal.cal:

  Calories consumed at meals

  wt.loss:

  Weight loss in last six months

  Terry Therneau

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cancer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 228 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cancer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/cancer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cancer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
