# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def help_miss(path):
  """Health Evaluation and Linkage to Primary Care

  The HELP study was a clinical trial for adult inpatients recruited from
  a detoxification unit. Patients with no primary care physician were
  randomized to receive a multidisciplinary assessment and a brief
  motivational intervention or usual care, with the goal of linking them
  to primary medical care.

  Data frame with 470 observations on the following variables.

  -  `age` subject age at baseline (in years)

  -  `anysub` use of any substance post-detox: a factor with levels
     `no` `yes`

  -  `cesd` Center for Epidemiologic Studies Depression measure of
     depressive symptoms at baseline (higher scores indicate more
     symptoms)

  -  `d1` lifetime number of hospitalizations for medical problems
     (measured at baseline)

  -  `daysanysub` time (in days) to first use of any substance
     post-detox

  -  `dayslink` time (in days) to linkage to primary care

  -  `drugrisk` Risk Assessment Battery drug risk scale at baseline

  -  `e2b` number of times in past 6 months entered a detox program
     (measured at baseline)

  -  `female` 0 for male, 1 for female

  -  `sex` a factor with levels `male` `female`

  -  `g1b` experienced serious thoughts of suicide in last 30 days
     (measured at baseline): a factor with levels `no` `yes`

  -  `homeless` housing status: a factor with levels `housed`
     `homeless`

  -  `i1` average number of drinks (standard units) consumed per day, in
     the past 30 days (measured at baseline)

  -  `i2` maximum number of drinks (standard units) consumed per day, in
     the past 30 days (measured at baseline)

  -  `id` subject identifier

  -  `indtot` Inventory of Drug Use Consequences (InDUC) total score
     (measured at baseline)

  -  `linkstatus` post-detox linkage to primary care (0 = no, 1 = yes)

  -  `link` post-detox linkage to primary care: `no` `yes`

  -  `mcs` SF-36 Mental Component Score (measured at baseline, higher
     scores are better)

  -  `pcs` SF-36 Physical Component Score (measured at baseline, higher
     scores are better)

  -  `pss_fr` perceived social support by friends (measured at baseline)

  -  `racegrp` race/ethnicity: levels `black` `hispanic` `other`
     `white`

  -  `satreat` any BSAS substance abuse treatment at baseline: `no`
     `yes`

  -  `sexrisk` Risk Assessment Battery sex risk score (measured at
     baseline)

  -  `substance` primary substance of abuse: `alcohol` `cocaine`
     `heroin`

  -  `treat` randomized to HELP clinic: `no` `yes`

  http://www.math.smith.edu/help

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `help_miss.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 470 rows and 25 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'help_miss.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/HELPmiss.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='help_miss.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
