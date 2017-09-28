# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def snails(path):
  """Snail Mortality Data

  Groups of 20 snails were held for periods of 1, 2, 3 or 4 weeks in
  carefully controlled conditions of temperature and relative humidity.
  There were two species of snail, A and B, and the experiment was
  designed as a 4 by 3 by 4 by 2 completely randomized design. At the end
  of the exposure time the snails were tested to see if they had survived;
  the process itself is fatal for the animals. The object of the exercise
  was to model the probability of survival in terms of the stimulus
  variables, and in particular to test for differences between species.

  The data are unusual in that in most cases fatalities during the
  experiment were fairly small.

  The data frame contains the following components:

  `Species`
      snail species A (`1`) or B (`2`).

  `Exposure`
      exposure in weeks.

  `Rel.Hum`
      relative humidity (4 levels).

  `Temp`
      temperature, in degrees Celsius (3 levels).

  `Deaths`
      number of deaths.

  `N`
      number of snails exposed.

  Zoology Department, The University of Adelaide.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `snails.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 96 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'snails.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/snails.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='snails.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
