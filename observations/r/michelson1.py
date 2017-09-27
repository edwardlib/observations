# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def michelson1(path):
  """Michelson's Speed of Light Data

  Measurements of the speed of light in air, made between 5th June and 2nd
  July, 1879. The data consists of five experiments, each consisting of 20
  consecutive runs. The response is the speed of light in km/s, less
  299000. The currently accepted value, on this scale of measurement, is
  734.5.

  The data frame contains the following components:

  `Expt`
      The experiment number, from 1 to 5.

  `Run`
      The run number within each experiment.

  `Speed`
      Speed-of-light measurement.

  A.J. Weekes (1986) *A Genstat Primer.* Edward Arnold.

  S. M. Stigler (1977) Do robust estimators work with real data? *Annals
  of Statistics* **5**, 1055–1098.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `michelson1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'michelson1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/michelson.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='michelson1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
