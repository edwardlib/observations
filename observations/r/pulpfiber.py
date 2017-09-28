# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pulpfiber(path):
  """Pulp Fiber and Paper Data

  Measurements of aspects pulp fibers and the paper produced from them.
  Four properties of each are measured in sixty-two samples.

  A data frame with 62 observations on the following 8 variables.

  `X1`
      numeric vector of arithmetic fiber length

  `X2`
      numeric vector of long fiber fraction

  `X3`
      numeric vector of fine fiber fraction

  `X4`
      numeric vector of zero span tensile

  `Y1`
      numeric vector of breaking length

  `Y2`
      numeric vector of elastic modulus

  `Y3`
      numeric vector of stress at failure

  `Y4`
      numeric vector of burst strength

  Rousseeuw, P. J., Van Aelst, S., Van Driessen, K., and Agulló, J. (2004)
  Robust multivariate regression; *Technometrics* **46**, 293–305.

  http://users.ugent.be/~svaelst/data/pulpfiber.txt

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pulpfiber.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pulpfiber.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/pulpfiber.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pulpfiber.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
