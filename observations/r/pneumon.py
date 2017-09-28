# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pneumon(path):
  """data from Section 1.13

  The `pneumon` data frame has 3470 rows and 15 columns.

  This data frame contains the following columns:

  chldage
      Age child had pneumonia, months

  hospital
      Indicator for hospitalization for pneumonia (1=yes, 0=no)

  mthage
      Age of the mother, years

  urban
      Urban environment for mother (1=yes, 0=no)

  alcohol
      Alcohol use by mother during pregnancy (1=yes, 0=no)

  smoke
      Cigarette use by mother during pregnancy (1=yes, 0=no)

  region
      Region of the coutry (1=northeast, 2=north central, 3=south, 4=west)

  poverty
      Mother at poverty level (1=yes, 0=no)

  bweight
      Normal birthweight (>5.5 lbs.) (1=yes, 0=no)

  race
      Race of the mother (1=white, 2=black, 3=other)

  education
      Education of the mother, years of school

  nsibs
      Number of siblings of the child

  wmonth
      Month the child was weaned

  sfmonth
      Month the child on solid food

  agepn
      Age child in the hospital for pneumonia, months

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. *National Longitudinal Survey of Youth
  Handbook* The Ohio State University, 1995.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pneumon.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3470 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pneumon.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/pneumon.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pneumon.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
