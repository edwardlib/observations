# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def liver(path):
  """Liver related laboratory data

  Liver related laboratory data from a randomized, blind, parallel group
  clinical trial with 4 doses of a drug.

  A data frame with 606 observations on the following 9 variables.

  ALP.B
      Alkaline phosphatase at baseline. A numeric vector.

  ALT.B
      Alanine aminotransferase at baseline. A numeric vector.

  AST.B
      Aspartate aminotransferase at baseline. A numeric vector.

  TBL.B
      Total bilirubin at baseline. A numeric vector.

  ALP.M
      Alkaline phosphatase after treatment. A numeric vector.

  ALT.M
      Alanine aminotransferase after treatment. A numeric vector.

  AST.M
      Aspartate aminotransferase after treatment. A numeric vector.

  TBL.M
      Total bilirubin after treatment. A numeric vector.

  dose
      The treatment group (i.e. dose group). A factor with levels `A`
      `B` `C` `D`


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `liver.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 606 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'liver.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/texmex/liver.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='liver.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
