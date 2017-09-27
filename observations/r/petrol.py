# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def petrol(path):
  """N. L. Prater's Petrol Refinery Data

  The yield of a petroleum refining process with four covariates. The
  crude oil appears to come from only 10 distinct samples.

  These data were originally used by Prater (1956) to build an estimation
  equation for the yield of the refining process of crude oil to gasoline.

  The variables are as follows

  `No`
      crude oil sample identification label. (Factor.)

  `SG`
      specific gravity, degrees API. (Constant within sample.)

  `VP`
      vapour pressure in pounds per square inch. (Constant within sample.)

  `V10`
      volatility of crude; ASTM 10% point. (Constant within sample.)

  `EP`
      desired volatility of gasoline. (The end point. Varies within
      sample.)

  `Y`
      yield as a percentage of crude.

  N. H. Prater (1956) Estimate gasoline yields from crudes. *Petroleum
  Refiner* **35**, 236–238.

  This dataset is also given in D. J. Hand, F. Daly, K. McConway, D. Lunn
  and E. Ostrowski (eds) (1994) *A Handbook of Small Data Sets.* Chapman &
  Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `petrol.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'petrol.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/petrol.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='petrol.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
