# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def verb_agg(path):
  """Verbal Aggression item responses

  These are the item responses to a questionaire on verbal aggression.
  These data are used throughout De Boeck and Wilson, *Explanatory Item
  Response Models* (Springer, 2004) to illustrate various forms of item
  response models.

  A data frame with 7584 observations on the following 13 variables.

  `Anger`
      the subject's Trait Anger score as measured on the State-Trait Anger
      Expression Inventory (STAXI)

  `Gender`
      the subject's gender - a factor with levels `M` and `F`

  `item`
      the item on the questionaire, as a factor

  `resp`
      the subject's response to the item - an ordered factor with levels
      `no` < `perhaps` < `yes`

  `id`
      the subject identifier, as a factor

  `btype`
      behavior type - a factor with levels `curse`, `scold` and
      `shout`

  `situ`
      situation type - a factor with levels `other` and `self`
      indicating other-to-blame and self-to-blame

  `mode`
      behavior mode - a factor with levels `want` and `do`

  `r2`
      dichotomous version of the response - a factor with levels `N` and
      `Y`

  http://bear.soe.berkeley.edu/EIRM/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `verb_agg.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7584 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'verb_agg.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/VerbAgg.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='verb_agg.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
