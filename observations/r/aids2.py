# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aids2(path):
  """Australian AIDS Survival Data

  Data on patients diagnosed with AIDS in Australia before 1 July 1991.

  This data frame contains 2843 rows and the following columns:

  `state`
      Grouped state of origin: `"NSW "`\ includes ACT and `"other"` is
      WA, SA, NT and TAS.

  `sex`
      Sex of patient.

  `diag`
      (Julian) date of diagnosis.

  `death`
      (Julian) date of death or end of observation.

  `status`
      `"A"` (alive) or `"D"` (dead) at end of observation.

  `T.categ`
      Reported transmission category.

  `age`
      Age (years) at diagnosis.

  Dr P. J. Solomon and the Australian National Centre in HIV Epidemiology
  and Clinical Research.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aids2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2843 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aids2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Aids2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aids2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
