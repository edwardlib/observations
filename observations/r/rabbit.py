# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rabbit(path):
  """Blood Pressure in Rabbits

  Five rabbits were studied on two occasions, after treatment with saline
  (control) and after treatment with the *5-HT\_3* antagonist MDL 72222.
  After each treatment ascending doses of phenylbiguanide were injected
  intravenously at 10 minute intervals and the responses of mean blood
  pressure measured. The goal was to test whether the cardiogenic
  chemoreflex elicited by phenylbiguanide depends on the activation of
  *5-HT\_3* receptors.

  This data frame contains 60 rows and the following variables:

  `BPchange`
      change in blood pressure relative to the start of the experiment.

  `Dose`
      dose of Phenylbiguanide in micrograms.

  `Run`
      label of run (`"C1"` to `"C5"`, then `"M1"` to `"M5"`).

  `Treatment`
      placebo or the *5-HT\_3* antagonist MDL 72222.

  `Animal`
      label of animal used (`"R1"` to `"R5"`).

  | J. Ludbrook (1994) Repeated measurements and multiple comparisons in
    cardiovascular research. *Cardiovascular Research* **28**, 303–311.
  | [The numerical data are not in the paper but were supplied by
    Professor Ludbrook]

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rabbit.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rabbit.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Rabbit.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rabbit.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
