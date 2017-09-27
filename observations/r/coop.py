# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def coop(path):
  """Co-operative Trial in Analytical Chemistry

  Seven specimens were sent to 6 laboratories in 3 separate batches and
  each analysed for Analyte. Each analysis was duplicated.

  This data frame contains the following columns:

  `Lab`
      Laboratory, `L1`, `L2`, ..., `L6`.

  `Spc`
      Specimen, `S1`, `S2`, ..., `S7`.

  `Bat`
      Batch, `B1`, `B2`, `B3` (nested within `Spc/Lab`),

  `Conc`
      Concentration of Analyte in *g/kg*.

  Analytical Methods Committee (1987) Recommendations for the conduct and
  interpretation of co-operative trials, *The Analyst* **112**, 679–686.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `coop.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 252 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'coop.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/coop.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='coop.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
