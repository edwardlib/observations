# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def survey(path):
  """Student Survey Data

  This data frame contains the responses of 237 Statistics I students at
  the University of Adelaide to a number of questions.

  The components of the data frame are:

  `Sex`
      The sex of the student. (Factor with levels `"Male"` and
      `"Female"`.)

  `Wr.Hnd`
      span (distance from tip of thumb to tip of little finger of spread
      hand) of writing hand, in centimetres.

  `NW.Hnd`
      span of non-writing hand.

  `W.Hnd`
      writing hand of student. (Factor, with levels `"Left"` and
      `"Right"`.)

  `Fold`
      “Fold your arms! Which is on top” (Factor, with levels `"R on L"`,
      `"L on R"`, `"Neither"`.)

  `Pulse`
      pulse rate of student (beats per minute).

  `Clap`
      ‘Clap your hands! Which hand is on top?’ (Factor, with levels
      `"Right"`, `"Left"`, `"Neither"`.)

  `Exer`
      how often the student exercises. (Factor, with levels `"Freq"`
      (frequently), `"Some"`, `"None"`.)

  `Smoke`
      how much the student smokes. (Factor, levels `"Heavy"`,
      `"Regul"` (regularly), `"Occas"` (occasionally), `"Never"`.)

  `Height`
      height of the student in centimetres.

  `M.I`
      whether the student expressed height in imperial (feet/inches) or
      metric (centimetres/metres) units. (Factor, levels `"Metric"`,
      `"Imperial"`.)

  `Age`
      age of the student in years.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `survey.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 237 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'survey.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/survey.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='survey.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
