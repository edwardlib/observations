# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crabs(path):
  """Morphological Measurements on Leptograpsus Crabs

  The `crabs` data frame has 200 rows and 8 columns, describing 5
  morphological measurements on 50 crabs each of two colour forms and both
  sexes, of the species *Leptograpsus variegatus* collected at Fremantle,
  W. Australia.

  This data frame contains the following columns:

  `sp`
      `species` - `"B"` or `"O"` for blue or orange.

  `sex`
      as it says.

  `index`
      index `1:50` within each of the four groups.

  `FL`
      frontal lobe size (mm).

  `RW`
      rear width (mm).

  `CL`
      carapace length (mm).

  `CW`
      carapace width (mm).

  `BD`
      body depth (mm).

  Campbell, N.A. and Mahon, R.J. (1974) A multivariate study of variation
  in two species of rock crab of genus *Leptograpsus.* *Australian Journal
  of Zoology* **22**, 417–425.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crabs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 200 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crabs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/crabs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crabs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
