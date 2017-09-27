# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_cereal(path):
  """Nutritional and Marketing Information on US Cereals

  The `UScereal` data frame has 65 rows and 11 columns. The data come
  from the 1993 ASA Statistical Graphics Exposition, and are taken from
  the mandatory F&DA food label. The data have been normalized here to a
  portion of one American cup.

  This data frame contains the following columns:

  `mfr`
      Manufacturer, represented by its first initial: G=General Mills,
      K=Kelloggs, N=Nabisco, P=Post, Q=Quaker Oats, R=Ralston Purina.

  `calories`
      number of calories in one portion.

  `protein`
      grams of protein in one portion.

  `fat`
      grams of fat in one portion.

  `sodium`
      milligrams of sodium in one portion.

  `fibre`
      grams of dietary fibre in one portion.

  `carbo`
      grams of complex carbohydrates in one portion.

  `sugars`
      grams of sugars in one portion.

  `shelf`
      display shelf (1, 2, or 3, counting from the floor).

  `potassium`
      grams of potassium.

  `vitamins`
      vitamins and minerals (none, enriched, or 100%).

  The original data are available at
  http://lib.stat.cmu.edu/datasets/1993.expo/.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_cereal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 65 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_cereal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/UScereal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_cereal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
