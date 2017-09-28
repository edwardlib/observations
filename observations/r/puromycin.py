# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def puromycin(path):
  """Reaction Velocity of an Enzymatic Reaction

  The `Puromycin` data frame has 23 rows and 3 columns of the reaction
  velocity versus substrate concentration in an enzymatic reaction
  involving untreated cells or cells treated with Puromycin.

  This data frame contains the following columns:

  `conc`
      a numeric vector of substrate concentrations (ppm)

  `rate`
      a numeric vector of instantaneous reaction rates (counts/min/min)

  `state`
      a factor with levels `treated` `untreated`

  Bates, D.M. and Watts, D.G. (1988), *Nonlinear Regression Analysis and
  Its Applications*, Wiley, Appendix A1.3.

  Treloar, M. A. (1974), *Effects of Puromycin on Galactosyltransferase in
  Golgi Membranes*, M.Sc. Thesis, U. of Toronto.

  See Also
  ~~~~~~~~

  `SSmicmen` for other models fitted to this dataset.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `puromycin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'puromycin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/Puromycin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='puromycin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
