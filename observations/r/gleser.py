# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gleser(path):
  """Example data from Gleser, Cronbach and Rajaratnam (1965) to show basic pri
  nciples of generalizability theory.

  Gleser, Cronbach and Rajaratnam (1965) discuss the estimation of
  variance components and their ratios as part of their introduction to
  generalizability theory. This is a adaptation of their "illustrative
  data for a completely matched G study" (Table 3). 12 patients are rated
  on 6 symptoms by two judges. Components of variance are derived from the
  ANOVA.

  A data frame with 12 observations on the following 12 variables. J item
  by judge:

  `J11`
      a numeric vector

  `J12`
      a numeric vector

  `J21`
      a numeric vector

  `J22`
      a numeric vector

  `J31`
      a numeric vector

  `J32`
      a numeric vector

  `J41`
      a numeric vector

  `J42`
      a numeric vector

  `J51`
      a numeric vector

  `J52`
      a numeric vector

  `J61`
      a numeric vector

  `J62`
      a numeric vector

  Gleser, G., Cronbach, L., and Rajaratnam, N. (1965). Generalizability of
  scores influenced by multiple sources of variance. Psychometrika,
  30(4):395-418. (Table 3, rearranged to show increasing patient severity
  and increasing item severity.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gleser.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gleser.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Gleser.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gleser.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
