# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def help_rct(path):
  """Health Evaluation and Linkage to Primary Care

  The HELP study was a clinical trial for adult inpatients recruited from
  a detoxification unit. Patients with no primary care physician were
  randomized to receive a multidisciplinary assessment and a brief
  motivational intervention or usual care, with the goal of linking them
  to primary medical care.

  Data frame with 453 observations on the following variables.

  -  `age` subject age at baseline (in years)

  -  `anysub` use of any substance post-detox: a factor with levels
     `no` `yes`

  -  `cesd` Center for Epidemiologic Studies Depression measure at
     baseline (high scores indicate more depressive symptoms)

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

  -  `mcs` SF-36 Mental Component Score (measured at baseline, lower
     scores indicate worse status)

  -  `pcs` SF-36 Physical Component Score (measured at baseline, lower
     scores indicate worse status)

  -  `pss_fr` perceived social support by friends (measured at baseline,
     higher scores indicate more support)

  -  `racegrp` race/ethnicity: levels `black` `hispanic` `other`
     `white`

  -  `satreat` any BSAS substance abuse treatment at baseline: `no`
     `yes`

  -  `sexrisk` Risk Assessment Battery sex risk score (measured at
     baseline)

  -  `substance` primary substance of abuse: `alcohol` `cocaine`
     `heroin`

  -  `treat` randomized to HELP clinic: `no` `yes`

  Details
  ~~~~~~~

  Eligible subjects were adults, who spoke Spanish or English, reported
  alcohol, heroin or cocaine as their first or second drug of choice,
  resided in proximity to the primary care clinic to which they would be
  referred or were homeless. Patients with established primary care
  relationships they planned to continue, significant dementia, specific
  plans to leave the Boston area that would prevent research
  participation, failure to provide contact information for tracking
  purposes, or pregnancy were excluded.

  Subjects were interviewed at baseline during their detoxification stay
  and follow-up interviews were undertaken every 6 months for 2 years. A
  variety of continuous, count, discrete, and survival time predictors and
  outcomes were collected at each of these five occasions.

  This data set is a subset of the `HELPmiss` data set restricted to the
  453 subjects who were fully observed on the `age`, `cesd`, `d1`,
  `female`, `sex`, `g1b`, `homeless`, `i1`, `i2`, `indtot`,
  `mcs`, `pcs`, `pss_fr`, `racegrp`, `satreat`, `substance`,
  `treat`, and `sexrisk` variables. (There is some missingness in the
  other variables.) `HELPmiss` contains 17 additional subjects with
  partially observed data on some of these baseline variables. This is
  also a subset of the `HELPfull` data which includes 5 timepoints and
  many additional variables.

  http://www.math.smith.edu/help

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `help_rct.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 453 rows and 27 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'help_rct.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/HELPrct.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='help_rct.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
