# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nwtco(path):
  """Data from the National Wilm's Tumor Study

  Measurement error example. Tumor histology predicts survival, but
  prediction is stronger with central lab histology than with the local
  institution determination.

  A data frame with 4028 observations on the following 9 variables.

  `seqno`
      id number

  `instit`
      Histology from local institution

  `histol`
      Histology from central lab

  `stage`
      Disease stage

  `study`
      study

  `rel`
      indicator for relapse

  `edrel`
      time to relapse

  `age`
      age in months

  `in.subcohort`
      Included in the subcohort for the example in the paper

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nwtco.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4028 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nwtco.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/nwtco.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nwtco.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
