# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cake(path):
  """Breakage Angle of Chocolate Cakes

  Data on the breakage angle of chocolate cakes made with three different
  recipes and baked at six different temperatures. This is a split-plot
  design with the recipes being whole-units and the different temperatures
  being applied to sub-units (within replicates). The experimental notes
  suggest that the replicate numbering represents temporal ordering.

  A data frame with 270 observations on the following 5 variables.

  `replicate`
      a factor with levels `1` to `15`

  `recipe`
      a factor with levels `A`, `B` and `C`

  `temperature`
      an ordered factor with levels `175` < `185` < `195` < `205`
      < `215` < `225`

  `angle`
      a numeric vector giving the angle at which the cake broke.

  `temp`
      numeric value of the baking temperature (degrees F).

  Original data were presented in Cook (1938), and reported in Cochran and
  Cox (1957, p. 300). Also cited in Lee, Nelder and Pawitan (2006).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cake.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 270 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cake.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/cake.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cake.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
