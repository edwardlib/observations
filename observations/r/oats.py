# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def oats(path):
  """Data from an Oats Field Trial

  The yield of oats from a split-plot field trial using three varieties
  and four levels of manurial treatment. The experiment was laid out in 6
  blocks of 3 main plots, each split into 4 sub-plots. The varieties were
  applied to the main plots and the manurial treatments to the sub-plots.

  This data frame contains the following columns:

  `B`
      Blocks, levels I, II, III, IV, V and VI.

  `V`
      Varieties, 3 levels.

  `N`
      Nitrogen (manurial) treatment, levels 0.0cwt, 0.2cwt, 0.4cwt and
      0.6cwt, showing the application in cwt/acre.

  `Y`
      Yields in 1/4lbs per sub-plot, each of area 1/80 acre.

  Yates, F. (1935) Complex experiments, *Journal of the Royal Statistical
  Society Suppl.* **2**, 181–247.

  Also given in Yates, F. (1970) *Experimental design: Selected papers of
  Frank Yates, C.B.E, F.R.S.* London: Griffin.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `oats.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'oats.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/oats.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='oats.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
