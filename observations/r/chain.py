# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chain(path):
  """Subset of variables from the CHAIN project

  The CHAIN project was a longitudinal cohort study of people living with
  HIV in New York City, which was recruited in 1994 from a large number of
  medical care and social service agencies serving HIV in New York City.
  This subset of data pertain to the sixth round of interviews.

  A `data.frame` with 532 observations on the following 8 variables.

  `log_virus`
      log of self reported viral load level, where zero represents an
      undetectable level.

  `age`
      age at time of the interview

  `income`
      annual family income in 10 intervals

  `healthy`
      a continuous scale of physical health with a theoretical range
      between 0 and 100 where better health is associated with higher
      scale values

  `mental`
      a binary measure of poor mental health ( 1=Yes, 0=No )

  `damage`
      ordered interval for the CD4 count, which is an indicator of how
      much damage HIV has caused to the immune system

  `treatment`
      a three-level ordered variable: 0=Not currently taking HAART (Highly
      Active AntiretRoviral Therapy) 1=taking HAART but nonadherent,
      2=taking HAART and adherent

  http://cchps.columbia.edu/research.cfm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chain.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 532 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chain.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mi/CHAIN.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chain.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
