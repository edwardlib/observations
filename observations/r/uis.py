# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def uis(path):
  """UIS Drug Treatment study data

  There are 628 data points in the original data, 575 of which have no
  missing values.

  Variable descriptions:

  +--------------------+--------------------------+--------------------------+
  | Variable           | Description              | Codes/Values             |
  +--------------------+--------------------------+--------------------------+
  | ID                 | Identification Code      | 1 - 628                  |
  +--------------------+--------------------------+--------------------------+
  | AGE                | Age at Enrollment        | Years                    |
  +--------------------+--------------------------+--------------------------+
  | BECK               | Beck DepressionScore     | 0.000 - 54.000           |
  +--------------------+--------------------------+--------------------------+
  | HC                 | Heroin/Cocaine Use       | 1 = Heroin & Cocaine     |
  |                    | During                   |                          |
  +--------------------+--------------------------+--------------------------+
  |                    | 3 Months Prior to        | 2 = Heroin Only          |
  |                    | Admission                |                          |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 3 = Cocaine Only         |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 4 = Neither Heroin nor   |
  |                    |                          | Cocaine                  |
  +--------------------+--------------------------+--------------------------+
  | IV                 | History of IV Drug Use   | 1 = Never                |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 2 = Previous             |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 3 = Recent               |
  +--------------------+--------------------------+--------------------------+
  | NDT                | Number of Prior Drug     | 0 - 40                   |
  |                    | Treatments               |                          |
  +--------------------+--------------------------+--------------------------+
  | RACE               | Subject's Race           | 0 = White                |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 1 = Non-White            |
  +--------------------+--------------------------+--------------------------+
  | TREAT              | Treatment Randomization  | 0 = Short                |
  +--------------------+--------------------------+--------------------------+
  |                    | Assignment               | 1 = Long                 |
  +--------------------+--------------------------+--------------------------+
  | SITE               | Treatment Site           | 0 = A                    |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 1 = B                    |
  +--------------------+--------------------------+--------------------------+
  | LEN.T              | Length of Stay in        | Days                     |
  |                    | Treatment                |                          |
  +--------------------+--------------------------+--------------------------+
  |                    | (Admission Date to Exit  |                          |
  |                    | Date)                    |                          |
  +--------------------+--------------------------+--------------------------+
  | TIME               | Time to Drug Relapse     | Days                     |
  +--------------------+--------------------------+--------------------------+
  |                    | (Measured from Admission |                          |
  |                    | Date)                    |                          |
  +--------------------+--------------------------+--------------------------+
  | CENSOR             | Event for Treating Lost  | 1 = Returned to Drugs    |
  |                    | to                       |                          |
  +--------------------+--------------------------+--------------------------+
  |                    | Follow-Up as Returned to | or Lost to Follow-Up     |
  |                    | Drugs                    |                          |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 0 = Otherwise            |
  +--------------------+--------------------------+--------------------------+
  | Y                  | log of TIME              |                          |
  +--------------------+--------------------------+--------------------------+
  | ND1                | Component of NDT         |                          |
  +--------------------+--------------------------+--------------------------+
  | ND2                | Component of NDT         |                          |
  +--------------------+--------------------------+--------------------------+
  | LNDT               |                          |                          |
  +--------------------+--------------------------+--------------------------+
  | FRAC               | Compliance fraction      | LEN.T/90 for short trt   |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | LEN.T/180 for long trt   |
  +--------------------+--------------------------+--------------------------+
  | IV3                | Recent IV use            | 1 = Yes                  |
  +--------------------+--------------------------+--------------------------+
  |                    |                          | 0 = No                   |
  +--------------------+--------------------------+--------------------------+

  A data frame with dimension 575 by 18.

  Table 1.3 of Hosmer,D.W. and Lemeshow, S. (1998)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `uis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 575 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'uis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/quantreg/uis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='uis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
