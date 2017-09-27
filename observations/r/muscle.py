# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def muscle(path):
  """Effect of Calcium Chloride on Muscle Contraction in Rat Hearts

  The purpose of this experiment was to assess the influence of calcium in
  solution on the contraction of heart muscle in rats. The left auricle of
  21 rat hearts was isolated and on several occasions a constant-length
  strip of tissue was electrically stimulated and dipped into various
  concentrations of calcium chloride solution, after which the shortening
  of the strip was accurately measured as the response.

  This data frame contains the following columns:

  `Strip`
      which heart muscle strip was used?

  `Conc`
      concentration of calcium chloride solution, in multiples of 2.2 mM.

  `Length`
      the change in length (shortening) of the strip, (allegedly) in mm.

  Linder, A., Chakravarti, I. M. and Vuagnat, P. (1964) Fitting asymptotic
  regression curves with different asymptotes. In *Contributions to
  Statistics. Presented to Professor P. C. Mahalanobis on the occasion of
  his 70th birthday*, ed. C. R. Rao, pp. 221–228. Oxford: Pergamon Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `muscle.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'muscle.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/muscle.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='muscle.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
