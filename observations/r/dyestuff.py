# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dyestuff(path):
  """Yield of dyestuff by batch

  The `Dyestuff` data frame provides the yield of dyestuff (Naphthalene
  Black 12B) from 5 different preparations from each of 6 different batchs
  of an intermediate product (H-acid). The `Dyestuff2` data were
  generated data in the same structure but with a large residual variance
  relative to the batch variance.

  Data frames, each with 30 observations on the following 2 variables.

  `Batch`
      a factor indicating the batch of the intermediate product from which
      the preparation was created.

  `Yield`
      the yield of dyestuff from the preparation (grams of standard
      color).

  O.L. Davies and P.L. Goldsmith (eds), *Statistical Methods in Research
  and Production, 4th ed.*, Oliver and Boyd, (1972), section 6.4

  G.E.P. Box and G.C. Tiao, *Bayesian Inference in Statistical Analysis*,
  Addison-Wesley, (1973), section 5.1.2

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dyestuff.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dyestuff.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/Dyestuff.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dyestuff.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
