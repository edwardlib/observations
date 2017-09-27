# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def std(path):
  """data from Section 1.12

  The `std` data frame has 877 rows and 3 columns.

  This data frame contains the following columns:

  obs
      Observation number

  race
      Race (W=white, B=black)

  marital
      Marital status (D=divorced / separated, M=married, S=single)

  age
      AGE

  yschool
      Years of schooling

  iinfct
      Initial infection (1= gonorrhea, 2=chlamydia, 3=both)

  npartner
      Number of partners

  os12m
      Oral sex within 12 months (1=yes, 0=no)

  os30d
      Oral sex within 30 days (1=yes, 0=no)

  rs12m
      Rectal sex within 12 months (1=yes, 0=no)

  rs30d
      Rectal sex within 30 days (1=yes, 0=no)

  abdpain
      Presence of abdominal pain (1=yes, 0=no)

  discharge
      Sign of discharge (1=yes, 0=no)

  dysuria
      Sign of dysuria (1=yes, 0=no)

  condom
      Condom use (1=always, 2=sometime, 3=never)

  itch
      Sign of itch (1=yes, 0=no)

  lesion
      Sign of lesion (1=yes, 0=no)

  rash
      Sign of rash (1=yes, 0=no)

  lymph
      Sign of lymph (1=yes, 0=no)

  vagina
      Involvement vagina at exam (1=yes, 0=no)

  dchexam
      Discharge at exam (1=yes, 0=no)

  abnode
      Abnormal node at exam (1=yes, 0=no)

  rinfct
      Reinfection (1=yes, 0=no)

  time
      Time to reinfection

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `std.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 877 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'std.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/std.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='std.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
