# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def penicillin(path):
  """Variation in penicillin testing

  Six samples of penicillin were tested using the *B. subtilis* plate
  method on each of 24 plates. The response is the diameter (mm) of the
  zone of inhibition of growth of the organism.

  A data frame with 144 observations on the following 3 variables.

  `diameter`
      diameter (mm) of the zone of inhibition of the growth of the
      organism.

  `plate`
      assay plate. A factor with levels ‘a’ to ‘x’.

  `sample`
      penicillin sample. A factor with levels ‘A’ to ‘F’.

  O.L. Davies and P.L. Goldsmith (eds), *Statistical Methods in Research
  and Production, 4th ed.*, Oliver and Boyd, (1972), section 6.6

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `penicillin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 144 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'penicillin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/Penicillin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='penicillin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
