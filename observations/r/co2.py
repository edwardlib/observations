# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def co2(path):
  """Carbon Dioxide Uptake in Grass Plants

  The `CO2` data frame has 84 rows and 5 columns of data from an
  experiment on the cold tolerance of the grass species *Echinochloa
  crus-galli*.

  An object of class
  `c("nfnGroupedData", "nfGroupedData", "groupedData", "data.frame")`
  containing the following columns:

  Plant
      an ordered factor with levels `Qn1` < `Qn2` < `Qn3` < ... <
      `Mc1` giving a unique identifier for each plant.

  Type
      a factor with levels `Quebec` `Mississippi` giving the origin of
      the plant

  Treatment
      a factor with levels `nonchilled` `chilled`

  conc
      a numeric vector of ambient carbon dioxide concentrations (mL/L).

  uptake
      a numeric vector of carbon dioxide uptake rates (*umol/m^2* sec).

  Potvin, C., Lechowicz, M. J. and Tardif, S. (1990) “The statistical
  analysis of ecophysiological response curves obtained from experiments
  involving repeated measures”, *Ecology*, **71**, 1389–1400.

  Pinheiro, J. C. and Bates, D. M. (2000) *Mixed-effects Models in S and
  S-PLUS*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `co2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 237 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'co2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/CO2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='co2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
