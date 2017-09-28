# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def farms(path):
  """Ecological Factors in Farm Management

  The `farms` data frame has 20 rows and 4 columns. The rows are farms
  on the Dutch island of Terschelling and the columns are factors
  describing the management of grassland.

  This data frame contains the following columns:

  `Mois`
      Five levels of soil moisture – level 3 does not occur at these 20
      farms.

  `Manag`
      Grassland management type (`SF` = standard, `BF` = biological,
      `HF` = hobby farming, `NM` = nature conservation).

  `Use`
      Grassland use (`U1` = hay production, `U2` = intermediate,
      `U3` = grazing).

  `Manure`
      Manure usage – classes `C0` to `C4`.

  J.C. Gower and D.J. Hand (1996) *Biplots*. Chapman & Hall, Table 4.6.

  | Quoted as from:
  | R.H.G. Jongman, C.J.F. ter Braak and O.F.R. van Tongeren (1987) *Data
    Analysis in Community and Landscape Ecology.* PUDOC, Wageningen.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `farms.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'farms.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/farms.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='farms.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
