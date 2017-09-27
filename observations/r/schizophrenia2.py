# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def schizophrenia2(path):
  """Schizophrenia Data

  Though disorder and early onset of schizophrenia.

  A data frame with 220 observations on the following 4 variables.

  `subject`
      the patient ID, a factor with levels `1` to `44`.

  `onset`
      the time of onset of the disease, a factor with levels `< 20 yrs`
      and `> 20 yrs`.

  `disorder`
      whether thought disorder was `absent` or `present`, the response
      variable.

  `month`
      month after hospitalisation.

  Davis (2002), *Statistical Methods for the Analysis of Repeated
  Measurements*, Springer, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `schizophrenia2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 220 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'schizophrenia2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/schizophrenia2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='schizophrenia2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
