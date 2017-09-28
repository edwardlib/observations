# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def epi_dictionary(path):
  """Eysenck Personality Inventory (EPI) data for 3570 participants

  The EPI is and has been a very frequently administered personality test
  with 57 measuring two broad dimensions, Extraversion-Introversion and
  Stability-Neuroticism, with an additional Lie scale. Developed by
  Eysenck and Eysenck, 1964. Eventually replaced with the EPQ which
  measures three broad dimensions. This data set represents 3570
  observations collected in the early 1990s at the Personality, Motivation
  and Cognition lab at Northwestern. The data are included here as
  demonstration of scale construction.

  A data frame with 3570 observations on the following 57 variables.

  `V1`
      a numeric vector

  `V2`
      a numeric vector

  `V3`
      a numeric vector

  `V4`
      a numeric vector

  `V5`
      a numeric vector

  `V6`
      a numeric vector

  `V7`
      a numeric vector

  `V8`
      a numeric vector

  `V9`
      a numeric vector

  `V10`
      a numeric vector

  `V11`
      a numeric vector

  `V12`
      a numeric vector

  `V13`
      a numeric vector

  `V14`
      a numeric vector

  `V15`
      a numeric vector

  `V16`
      a numeric vector

  `V17`
      a numeric vector

  `V18`
      a numeric vector

  `V19`
      a numeric vector

  `V20`
      a numeric vector

  `V21`
      a numeric vector

  `V22`
      a numeric vector

  `V23`
      a numeric vector

  `V24`
      a numeric vector

  `V25`
      a numeric vector

  `V26`
      a numeric vector

  `V27`
      a numeric vector

  `V28`
      a numeric vector

  `V29`
      a numeric vector

  `V30`
      a numeric vector

  `V31`
      a numeric vector

  `V32`
      a numeric vector

  `V33`
      a numeric vector

  `V34`
      a numeric vector

  `V35`
      a numeric vector

  `V36`
      a numeric vector

  `V37`
      a numeric vector

  `V38`
      a numeric vector

  `V39`
      a numeric vector

  `V40`
      a numeric vector

  `V41`
      a numeric vector

  `V42`
      a numeric vector

  `V43`
      a numeric vector

  `V44`
      a numeric vector

  `V45`
      a numeric vector

  `V46`
      a numeric vector

  `V47`
      a numeric vector

  `V48`
      a numeric vector

  `V49`
      a numeric vector

  `V50`
      a numeric vector

  `V51`
      a numeric vector

  `V52`
      a numeric vector

  `V53`
      a numeric vector

  `V54`
      a numeric vector

  `V55`
      a numeric vector

  `V56`
      a numeric vector

  `V57`
      a numeric vector

  Data from the PMC laboratory at Northwestern.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `epi_dictionary.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 57 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'epi_dictionary.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/epi.dictionary.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='epi_dictionary.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
