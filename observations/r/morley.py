# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def morley(path):
  """Michelson Speed of Light Data

  A classical data of Michelson (but not this one with Morley) on
  measurements done in 1879 on the speed of light. The data consists of
  five experiments, each consisting of 20 consecutive ‘runs’. The response
  is the speed of light measurement, suitably coded (km/sec, with
  `299000` subtracted).

  A data frame with 100 observations on the following 3 variables.

  `Expt`
      The experiment number, from 1 to 5.

  `Run`
      The run number within each experiment.

  `Speed`
      Speed-of-light measurement.

  Details
  ~~~~~~~

  The data is here viewed as a randomized block experiment with
  ‘experiment’ and ‘run’ as the factors. ‘run’ may also be considered a
  quantitative variate to account for linear (or polynomial) changes in
  the measurement over the course of a single experiment.

  A. J. Weekes (1986) *A Genstat Primer*. London: Edward Arnold.

  S. M. Stigler (1977) Do robust estimators work with real data? *Annals
  of Statistics* **5**, 1055–1098. (See Table 6.)

  A. A. Michelson (1882) Experimental determination of the velocity of
  light made at the United States Naval Academy, Annapolis. *Astronomic
  Papers* **1** 135–8. U.S. Nautical Almanac Office. (See Table 24.)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `morley.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'morley.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/morley.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='morley.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
