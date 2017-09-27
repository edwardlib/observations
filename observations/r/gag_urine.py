# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gag_urine(path):
  """Level of GAG in Urine of Children

  Data were collected on the concentration of a chemical GAG in the urine
  of 314 children aged from zero to seventeen years. The aim of the study
  was to produce a chart to help a paediatrican to assess if a child's GAG
  concentration is ‘normal’.

  This data frame contains the following columns:

  `Age`
      age of child in years.

  `GAG`
      concentration of GAG (the units have been lost).

  Mrs Susan Prosser, Paediatrics Department, University of Oxford, via
  Department of Statistics Consulting Service.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gag_urine.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 314 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gag_urine.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/GAGurine.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gag_urine.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
