# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mgus(path):
  """Monoclonal gammapothy data

  Natural history of 241 subjects with monoclonal gammapothy of
  undetermined significance (MGUS).

  mgus: A data frame with 241 observations on the following 12 variables.

  id:

  subject id

  age:

  age in years at the detection of MGUS

  sex:

  `male` or `female`

  dxyr:

  year of diagnosis

  pcdx:

  for subjects who progress to a plasma cell malignancy

  the subtype of malignancy: multiple myeloma (MM) is the

  most common, followed by amyloidosis (AM), macroglobulinemia (MA),

  and other lymphprolifative disorders (LP)

  pctime:

  days from MGUS until diagnosis of a plasma cell malignancy

  futime:

  days from diagnosis to last follow-up

  death:

  1= follow-up is until death

  alb:

  albumin level at MGUS diagnosis

  creat:

  creatinine at MGUS diagnosis

  hgb:

  hemoglobin at MGUS diagnosis

  mspike:

  size of the monoclonal protein spike at diagnosis

  mgus1: The same data set in start,stop format. Contains the id, age,
  sex, and laboratory variable described above along with

+----------------+----------------------------------------------------------+
| start, stop:   | sequential intervals of time for each subject            |
+----------------+----------------------------------------------------------+
| status:        | =1 if the interval ends in an event                      |
+----------------+----------------------------------------------------------+
| event:         | a factor containing the event type: censor, death,       |
|                | or plasma cell malignancy                                |
+----------------+----------------------------------------------------------+
| enum:          | event number for each subject: 1 or 2                    |
+----------------+----------------------------------------------------------+

  Mayo Clinic data courtesy of Dr. Robert Kyle.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mgus.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 241 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mgus.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/mgus.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mgus.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
