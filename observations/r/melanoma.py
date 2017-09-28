# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def melanoma(path):
  """Melanoma skin cancer incidence

  These data from the Connecticut Tumor Registry present age-adjusted
  numbers of melanoma skin-cancer incidences per 100,000 people in
  Connectict for the years from 1936 to 1972.

  A data frame with 37 observations on the following 2 variables.

  year
      Years 1936 to 1972.

  incidence
      Rate of melanoma cancer per 100,000 population.

  Houghton, A., E. W. Munster, and M. V. Viola. (1978). Increased
  Incidence of Malignant Melanoma After Peaks of Sunspot Activity. *The
  Lancet*, **8**, 759–760.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `melanoma.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'melanoma.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lattice/melanoma.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='melanoma.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
