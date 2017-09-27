# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ex_am(path):
  """Example Data of Antille and May - for Simple Regression

  This is an artificial data set, cleverly construced and used by Antille
  and May to demonstrate ‘problems’ with LMS and LTS.

  A data frame with 12 observations on 2 variables, `x` and `y`.

  | Antille, G. and El May, H. (1992) The use of slices in the LMS and the
    method of density slices: Foundation and comparison.
  | In Yadolah Dodge and Joe Whittaker, editors, *COMPSTAT: Proc. 10th
    Symp. Computat. Statist., Neuchatel*, **1**, 441–445; Physica-Verlag.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ex_am.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ex_am.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/exAM.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ex_am.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
