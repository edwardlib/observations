# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def n_cbirths(path):
  """NCbirths

  Data from births in North Carolina in 2001

  A dataset with 1450 observations on the following 15 variables.

  `ID`

  Patient ID code

  `Plural`

  `1`\ =single birth, `2`\ =twins, `3`\ =triplets

  `Sex`

  Sex of the baby `1`\ =male `2`\ =female

  `MomAge`

  Mother's age (in years)

  `Weeks`

  Completed weeks of gestation

  `Marital`

  Marital status: `1`\ =married or `2`\ =not married

  `RaceMom`

  Mother's race: `1`\ =white, `2`\ =black, `3`\ =American Indian,
  `4`\ =Chinese

  `5`\ =Japanese, `6`\ =Hawaiian, `7`\ =Filipino, or `8`\ =Other
  Asian or Pacific Islander

  `HispMom`

  Hispanic origin of mother: `C`\ =Cuban, `M`\ =Mexican, `N`\ =not
  Hispanic

  `O`\ =Other Hispanic, `P`\ =Puerto Rico, `S`\ =Central/South
  America

  `Gained`

  Weight gained during pregnancy (in pounds)

  `Smoke`

  Smoker mom? `1`\ =yes or `0`\ =no

  `BirthWeightOz`

  Birth weight in ounces

  `BirthWeightGm`

  Birth weight in grams

  `Low`

  Indicator for low birth weight, `1`\ =2500 grams or less

  `Premie`

  Indicator for premature birth, `1`\ =36 weeks or sooner

  `MomRace`

  Mother's race: `black`, `hispanic`, `other`, or `white`

  Thanks to John Holcomb at Cleveland State University for sharing these

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `n_cbirths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1450 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'n_cbirths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/NCbirths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='n_cbirths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
