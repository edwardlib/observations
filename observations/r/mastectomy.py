# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mastectomy(path):
  """Survival Times after Mastectomy of Breast Cancer Patients

  Survival times in months after mastectomy of women with breast cancer.
  The cancers are classified as having metastized or not based on a
  histochemical marker.

  A data frame with 42 observations on the following 3 variables.

  time
      survival times in months.

  event
      a logical indicating if the event was observed (`TRUE`) or if the
      survival time was censored (`FALSE`).

  metastized
      a factor at levels `yes` and `no`.

  B. S. Everitt and S. Rabe-Hesketh (2001), *Analysing Medical Data using
  S-PLUS*, Springer, New York, USA.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mastectomy.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 44 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mastectomy.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/mastectomy.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mastectomy.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
