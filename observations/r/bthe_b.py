# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bthe_b(path):
  """Beat the Blues Data

  Data from a clinical trial of an interactive multimedia program called
  ‘Beat the Blues’.

  A data frame with 100 observations of 100 patients on the following 8
  variables.

  drug
      did the patient take anti-depressant drugs (`No` or `Yes`).

  length
      the length of the current episode of depression, a factor with
      levels `<6m` (less than six months) and `>6m` (more than six
      months).

  treatment
      treatment group, a factor with levels `TAU` (treatment as usual)
      and `BtheB` (Beat the Blues)

  bdi.pre
      Beck Depression Inventory II before treatment.

  bdi.2m
      Beck Depression Inventory II after two months.

  bdi.4m
      Beck Depression Inventory II after four months.

  bdi.6m
      Beck Depression Inventory II after six months.

  bdi.8m
      Beck Depression Inventory II after eight months.

  J. Proudfoot, D. Goldberg and A. Mann (2003). Computerised, interactive,
  multimedia CBT reduced anxiety and depression in general practice: A
  RCT. *Psychological Medicine*, **33**, 217–227.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bthe_b.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bthe_b.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/BtheB.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bthe_b.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
