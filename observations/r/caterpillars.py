# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def caterpillars(path):
  """Caterpillars

  Measurements on a sample of Manduca Sexta caterpillars

  A dataset with 267 observations on the following 18 variables.

  `Instar`

  Coded from 1 (smallest) to 5 (largest) indicating stage of the
  caterpillar's life

  `ActiveFeeding`

  Indicator (`Y` or `N`) of whether or not the animal is actively
  feeding

  `Fgp`

  Indicator (`Y` or `N`) of whether or not the animal is in a free
  growth period

  `Mgp`

  Indicator (`Y` or `N`) of whether or not the animal is in a maximum
  growth period

  `Mass`

  Body mass (in grams)

  `LogMass`

  Log (base 10) of body mass

  `Intake`

  Wet food intake (in grams/day)

  `LogIntake`

  Log (base 10) of Intake

  `WetFrass`

  Amount of frass (solid waste) produced (in grams/day)

  `LogWetFrass`

  Log (base 10) of WetFrass

  `DryFrass`

  Amount of frass, after drying, produced (in grams/day)

  `LogDryFrass`

  Log (base 10) of DryFrass

  `Cassim`

  CO2 assimilation (ingestion - excretion)

  `LogCassim`

  Log (base 10) of Cassim

  `Nfrass`

  Nitrogen in frass

  `LogNfrass`

  Log (base 10) of Nfrass

  `Nassim`

  Nitrogen assimilation (ingestion - excretion)

  `LogNassim`

  Log (base 10) of Nassim

  We thank Professors Harry Itagaki, Drew Kerkhoff, Chris Gillen, and Judy
  Holdener and their students for sharing this data from research

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `caterpillars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 267 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'caterpillars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Caterpillars.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='caterpillars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
