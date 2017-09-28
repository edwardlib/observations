# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def arabidopsis(path):
  """Arabidopsis clipping/fertilization data

  Data on genetic variation in responses to fertilization and simulated
  herbivory in *Arabidopsis*

  A data frame with 625 observations on the following 8 variables.

  `reg`
      region: a factor with 3 levels `NL` (Netherlands), `SP` (Spain),
      `SW` (Sweden)

  `popu`
      population: a factor with the form `n.R` representing a population
      in region `R`

  `gen`
      genotype: a factor with 24 (numeric-valued) levels

  `rack`
      a nuisance factor with 2 levels, one for each of two greenhouse
      racks

  `nutrient`
      fertilization treatment/nutrient level (1, minimal nutrients or 8,
      added nutrients)

  `amd`
      simulated herbivory or "clipping" (apical meristem damage):
      `unclipped` (baseline) or `clipped`

  `status`
      a nuisance factor for germination method (`Normal`,
      `Petri.Plate`, or `Transplant`)

  `total.fruits`
      total fruit set per plant (integer)

  From Josh Banta

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `arabidopsis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 625 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'arabidopsis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/Arabidopsis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='arabidopsis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
