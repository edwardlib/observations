# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def epi_bfi(path):
  """13 personality scales from the Eysenck Personality Inventory and Big 5 inv
  entory

  A small data set of 5 scales from the Eysenck Personality Inventory, 5
  from a Big 5 inventory, a Beck Depression Inventory, and State and Trait
  Anxiety measures. Used for demonstrations of correlations, regressions,
  graphic displays.

  A data frame with 231 observations on the following 13 variables.

  `epiE`
      EPI Extraversion

  `epiS`
      EPI Sociability (a subset of Extraversion items

  `epiImp`
      EPI Impulsivity (a subset of Extraversion items

  `epilie`
      EPI Lie scale

  `epiNeur`
      EPI neuroticism

  `bfagree`
      Big 5 inventory (from the IPIP) measure of Agreeableness

  `bfcon`
      Big 5 Conscientiousness

  `bfext`
      Big 5 Extraversion

  `bfneur`
      Big 5 Neuroticism

  `bfopen`
      Big 5 Openness

  `bdi`
      Beck Depression scale

  `traitanx`
      Trait Anxiety

  `stateanx`
      State Anxiety

  Data were collected at the Personality, Motivation, and Cognition Lab
  (PMCLab) at Northwestern by William Revelle)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `epi_bfi.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 231 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'epi_bfi.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/epi.bfi.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='epi_bfi.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
