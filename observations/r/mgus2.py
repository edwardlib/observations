# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mgus2(path):
  """Monoclonal gammapothy data

  Natural history of 1341 sequential patients with monoclonal gammapothy
  of undetermined significance (MGUS).

  A data frame with 1384 observations on the following 10 variables.

  `id`
      subject identifier

  `age`
      age at diagnosis, in years

  `sex`
      a factor with levels `F` `M`

  `hgb`
      hemoglobin

  `creat`
      creatinine

  `mspike`
      size of the monoclonal serum splike

  `ptime`
      time until progression to a plasma cell malignancy (PCM) or last
      contact, in months

  `pstat`
      occurrence of PCM: 0=no, 1=yes

  `futime`
      time until death or last contact, in months

  `death`
      occurrence of death: 0=no, 1=yes

  Mayo Clinic data courtesy of Dr. Robert Kyle. All patient identifiers
  have been removed, age rounded to the nearest year, and follow-up times
  rounded to the nearest month.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mgus2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1384 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mgus2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/mgus2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mgus2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
