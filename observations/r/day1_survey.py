# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def day1_survey(path):
  """Day1Survey

  Data from a first day class survey

  A dataset with 43 observations on the following 13 variables.

  `Section`

  Section: `1` or `2`

  `Class`

  Year in school: `Freshman`, `Sophomore`, `Junior`, or `Senior`

  `Sex`

  `F`\ =female or `M`\ =male

  `Distance`

  Distance (in miles) to get to campus

  `Height`

  Height (in inches)

  `Handedness`

  `Left`, `Right`, or `Ambidextrous`

  `Coins`

  Value of coins student has (in class)

  `WhiteString`

  Estimated length of a white string (in inches)

  `BlackString`

  Estimated length of a black string (in inches)

  `Reading`

  Expected amount of reading during the semester (pages/week)

  `TV`

  Hours of TV watched per week

  `Pulse`

  Resting pulse rate (beats per minute)

  `Texting`

  Number of text messages in past 24 hours


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `day1_survey.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 43 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'day1_survey.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Day1Survey.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='day1_survey.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
