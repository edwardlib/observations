# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def polio_trials(path):
  """Polio Field Trials Data

  The data frame `PolioTrials` gives the results of the 1954 field
  trials to test the Salk polio vaccine (named for the developer, Jonas
  Salk), conducted by the National Foundation for Infantile Paralysis
  (NFIP). It is adapted from data in the article by Francis et al. (1955).
  There were actually two clinical trials, corresponding to two
  statistical designs (`Experiment`), discussed by Brownlee (1955). The
  comparison of designs and results represented a milestone in the
  development of randomized clinical trials.

  A data frame with 8 observations on the following 6 variables.

  `Experiment`
      a factor with levels `ObservedControl` `RandomizedControl`

  `Group`
      a factor with levels `Controls` `Grade2NotInoculated`
      `IncompleteVaccinations` `NotInoculated` `Placebo`
      `Vaccinated`

  `Population`
      the size of the population in each group in each experiment

  `Paralytic`
      the number of cases of paralytic polio observed in that group

  `NonParalytic`
      the number of cases of paralytic polio observed in that group

  `FalseReports`
      the number of cases initially reported as polio, but later
      determined not to be polio in that group

  Kyle Siegrist, "Virtual Laboratories in Probability and Statistics",
  http://www.math.uah.edu/stat/data/Polio.html

  Thomas Francis, Robert Korn, et al. (1955). "An Evaluation of the 1954
  Poliomyelitis Vaccine Trials", *American Journal of Public Health*, 45,
  (50 page supplement with a 63 page appendix).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `polio_trials.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'polio_trials.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/PolioTrials.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='polio_trials.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
