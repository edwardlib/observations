# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bod(path):
  """Biochemical Oxygen Demand

  The `BOD` data frame has 6 rows and 2 columns giving the biochemical
  oxygen demand versus time in an evaluation of water quality.

  This data frame contains the following columns:

  `Time`
      A numeric vector giving the time of the measurement (days).

  `demand`
      A numeric vector giving the biochemical oxygen demand (mg/l).

  Bates, D.M. and Watts, D.G. (1988), *Nonlinear Regression Analysis and
  Its Applications*, Wiley, Appendix A1.4.

  Originally from Marske (1967), *Biochemical Oxygen Demand Data
  Interpretation Using Sum of Squares Surface* M.Sc. Thesis, University of
  Wisconsin – Madison.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bod.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bod.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/BOD.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bod.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
