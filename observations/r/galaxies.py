# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def galaxies(path):
  """Velocities for 82 Galaxies

  A numeric vector of velocities in km/sec of 82 galaxies from 6
  well-separated conic sections of an `unfilled` survey of the Corona
  Borealis region. Multimodality in such surveys is evidence for voids and
  superclusters in the far universe.

  Roeder, K. (1990) Density estimation with confidence sets exemplified by
  superclusters and voids in galaxies. *Journal of the American
  Statistical Association* **85**, 617–624.

  Postman, M., Huchra, J. P. and Geller, M. J. (1986) Probes of
  large-scale structures in the Corona Borealis region. *Astronomical
  Journal* **92**, 1238–1247.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `galaxies.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 82 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'galaxies.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/galaxies.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='galaxies.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
