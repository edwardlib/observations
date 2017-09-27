# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def unemployment(path):
  """Unemployment Duration

  a cross-section from 1993

  *number of observations* : 452

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  duration
      duration of first spell of unemployment, t, in weeks

  spell
      1 if spell is complete

  race
      one of nonwhite, white

  sex
      one of male, female

  reason
      reason for unemployment, one of new (new entrant), lose (job loser),
      leave (job leaver), reentr (labor force reentrant)

  search
      'yes' if (1) the unemployment spell is completed between the first
      and second surveys and number of methods used to search > average
      number of methods used across all records in the sample, or, (2) for
      individuals who remain unemployed for consecutive surveys, if the
      number of methods used is strictly nondecreasing at all survey
      points, and is strictly increasing at least at one survey point

  pubemp
      'yes' if an individual used a public employment agency to search for
      work at any survey points relating to the individuals first
      unemployment spell

  ftp1
      1 if an individual is searching for full time work at survey 1

  ftp2
      1 if an individual is searching for full time work at survey 2

  ftp3
      1 if an individual is searching for full time work at survey 3

  ftp4
      1 if an individual is searching for full time work at survey 4

  nobs
      number of observations on the first spell of unemployment for the
      record

  Romeo, Charles J. (1999) “Conducting inference in semiparametric
  duration models under inequality restrictions on the shape of the hazard
  implied by the job search theory”, *Journal of Applied Econometrics*,
  **14(6)**, 587–605.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `unemployment.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 452 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'unemployment.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Unemployment.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='unemployment.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
