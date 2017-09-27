# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def head_injury(path):
  """Minor Head Injury (Simulated) Data

  The `head.injury` data frame has 3121 rows and 11 columns. The data
  were simulated according to a simple logistic regression model to match
  roughly the clinical characteristics of a sample of individuals who
  suffered minor head injuries.

  This data frame contains the following columns:

  age.65
      age factor (0 = under 65, 1 = over 65).

  amnesia.before
      amnesia before impact (less than 30 minutes = 0, more than 30
      minutes =1).

  basal.skull.fracture
      (0 = no fracture, 1 = fracture).

  GCS.decrease
      Glasgow Coma Scale decrease (0 = no deterioration, 1 =
      deterioration).

  GCS.13
      initial Glasgow Coma Scale (0 = not ‘13’, 1 = ‘13’).

  GCS.15.2hours
      Glasgow Coma Scale after 2 hours (0 = not ‘15’, 1 = '15').

  high.risk
      assessed by clinician as high risk for neurological intervention (0
      = not high risk, 1 = high risk).

  loss.of.consciousness
      (0 = conscious, 1 = loss of consciousness).

  open.skull.fracture
      (0 = no fracture, 1 = fracture)

  vomiting
      (0 = no vomiting, 1 = vomiting)

  clinically.important.brain.injury
      any acute brain finding revealed on CT (0 = not present, 1 =
      present).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `head_injury.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3121 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'head_injury.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/head.injury.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='head_injury.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
