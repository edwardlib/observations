# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def parkinsons(path):
  """A study of Parkinson's disease and APOE, LRRK2, SNCA makers

  A study of Parkinson's disease and controls with APOE, LRRK2 markers
  rs10506151, rs10784486, rs1365763, rs1388598, rs1491938, rs1491941 and
  SNCA markers m770, int4 and SNCA. The column abc indicates if a subject
  is familial Parkinson's (+), sporadic (-), or controls (Control). Races
  involved are American Indians (AI), African American (B), and the rest
  are Caucasians. Diagnosis also included possible (POS), probable (PRO)
  and definite PDs. AON is the age at onset.

  A data frame

  Prof Abbas Parsian at NIH

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `parkinsons.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 825 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'parkinsons.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/PD.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='parkinsons.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
