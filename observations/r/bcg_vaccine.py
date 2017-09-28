# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bcg_vaccine(path):
  """BCG Vaccine Data

  A meta-analysis on the efficacy of BCG vaccination against tuberculosis
  (TB).

  A data frame with 13 observations on the following 7 variables.

  `Study`
      an identifier of the study.

  `BCGTB`
      the number of subjects suffering from TB after a BCG vaccination.

  `BCGVacc`
      the number of subjects with BCG vaccination.

  `NoVaccTB`
      the number of subjects suffering from TB without BCG vaccination.

  `NoVacc`
      the total number of subjects without BCG vaccination.

  `Latitude`
      geographic position of the place the study was undertaken.

  `Year`
      the year the study was undertaken.

  G. A. Colditz, T. F. Brewer, C. S. Berkey, M. E. Wilson, E. Burdick, H.
  V. Fineberg and F. Mosteller (1994), Efficacy of BCG vaccine in the
  prevention of tuberculosis. Meta-analysis of the published literature.
  *Journal of the American Medical Association*, **271**\ (2), 698–702.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bcg_vaccine.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 13 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bcg_vaccine.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/BCG.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bcg_vaccine.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
