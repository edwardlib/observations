# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def icu(path):
  """ICU

  Patients at an Intensive Care Unit (ICU)

  A dataset with 200 observations on the following 9 variables.

  `ID`

  Patient ID code

  `Survive`

  `1`\ =patient survived to discharge or `0`\ =patient died

  `Age`

  Age (in years)

  `AgeGroup`

  `1`\ = young (under 50), `2`\ = middle (50-69), `3` = old (70+)

  `Sex`

  `1`\ =female or `0`\ =male

  `Infection`

  `1`\ =infection suspected or `0`\ =no infection

  `SysBP`

  Systolic blood pressure (in mm of Hg)

  `Pulse`

  Hear rate4 (beats per minute)

  `Emergency`

  `1`\ =emergency admission or `0`\ =elective admission

  Data downladed from The Data and Story Library (DASL),

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `icu.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 200 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'icu.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/ICU.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='icu.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
