# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def galton2(path):
  """Galton's dataset of parent and child heights

  In the 1880's, Francis Galton was developing ways to quantify the
  heritability of traits. As part of this work, he collected data on the
  heights of adult children and their parents.

  A data frame with 898 observations on the following variables.

  -  `family` a factor with levels for each family

  -  `father` the father's height (in inches)

  -  `mother` the mother's height (in inches)

  -  `sex` the child's sex: `F` or `M`

  -  `height` the child's height as an adult (in inches)

  -  `nkids` the number of adult children in the family, or, at least,
     the number whose heights Galton recorded.

  The data were transcribed by J.A. Hanley who has published them at
  http://www.medicine.mcgill.ca/epidemiology/hanley/galton/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `galton2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 898 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'galton2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Galton.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='galton2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
