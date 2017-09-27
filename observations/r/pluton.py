# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pluton(path):
  """Isotopic Composition Plutonium Batches

  The `pluton` data frame has 45 rows and 4 columns, containing
  percentages of isotopic composition of 45 Plutonium batches.

  This data frame contains the following columns:

  Pu238
      the percentages of *(238)Pu*, always less than 2 percent.

  Pu239
      the percentages of *(239)Pu*, typically between 60 and 80 percent
      (from neutron capture of Uranium, *(238)U*).

  Pu240
      percentage of the plutonium 240 isotope.

  Pu241
      percentage of the plutonium 241 isotope.

  Available as ‘pluton.dat’ from the archive of the University of
  Antwerpen, ‘..../datasets/clusplot-examples.tar.gz’, no longer
  available.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pluton.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pluton.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/pluton.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pluton.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
