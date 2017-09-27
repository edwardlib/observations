# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def olives(path):
  """Olives

  Measurements of the pesticide fenthion in olive oil over time

  A dataset with 18 observations on the following 7 variables.

  `SampleNumber`

  Code (1-6) for sample of olive oil

  `Group`

  Code for group: `1` or `2`

  `Day`

  Time (in days) when sample was measured: `0`, `281`, or `365`

  `Fenthion`

  Amount of fenthion (pesticide)

  `FenthionSulphoxide`

  Amount of fenthion sulfide

  `FenthionSulphone`

  Amount of fenthion sulphone

  `Time`

  Code (0, 3, or 4) for the number of days

  Data provided by Rosemary Roberts and discussed in "Persistence of
  fenthion residues in olive oil" by Chaido Lentza-Rizos, Elizabeth J.
  Avramides, and Rosemary A. Roberts in Pest Management Science, Vol. 40,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `olives.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'olives.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Olives.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='olives.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
