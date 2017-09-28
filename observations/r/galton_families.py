# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def galton_families(path):
  """Galton's data on the heights of parents and their children, by child

  This data set lists the individual observations for 934 children in 205
  families on which Galton (1886) based his cross-tabulation.

  In addition to the question of the relation between heights of parents
  and their offspring, for which this data is mainly famous, Galton had
  another purpose which the data in this form allows to address: Does
  marriage selection indicate a relationship between the heights of
  husbands and wives, a topic he called *assortative mating*? Keen [p.
  297-298](2010) provides a brief discussion of this topic.

  A data frame with 934 observations on the following 8 variables.

  `family`
      family ID, a factor with levels `001`-`204`

  `father`
      height of father

  `mother`
      height of mother

  `midparentHeight`
      mid-parent height, calculated as `(father + 1.08*mother)/2`

  `children`
      number of children in this family

  `childNum`
      number of this child within family. Children are listed in
      decreasing order of height for boys followed by girls

  `gender`
      child gender, a factor with levels `female` `male`

  `childHeight`
      height of child

  Galton's notebook,
  http://www.medicine.mcgill.ca/epidemiology/hanley/galton/notebook/,
  transcribed by Beverley Shipley in 2001.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `galton_families.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 934 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'galton_families.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/GaltonFamilies.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='galton_families.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
