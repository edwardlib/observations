# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def youth_risk2007(path):
  """YouthRisk2007

  Risky behavior (riding with a drnk driver) in youths

  A dataset with 13387 observations on the following 6 variables.

  `ride.alc.driver`

  `1`\ =rode with a drinking driver in past 30 days or `0`\ =did not

  `female`

  `1`\ =female or `0`\ =male

  `grade`

  Year in high school: `9`, `10`, `11`, or `12`

  `age4`

  Age (in years)

  `smoke`

  Ever smoked? `1`\ =yes or `0`\ =no

  `DriverLicense`

  Have a driver's license? `1`\ =yes or `0`\ =no

  The article "Which Young People Accept a Lift From a Drunk or Drugged
  Driver?" in Accident Analysis and Prevention (July 2009. pp. 703-9)
  provides more details.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `youth_risk2007.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 13387 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'youth_risk2007.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/YouthRisk2007.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='youth_risk2007.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
