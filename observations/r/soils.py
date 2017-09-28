# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def soils(path):
  """Soil Compositions of Physical and Chemical Characteristics

  Soil characteristics were measured on samples from three types of
  contours (Top, Slope, and Depression) and at four depths (0-10cm,
  10-30cm, 30-60cm, and 60-90cm). The area was divided into 4 blocks, in a
  randomized block design. (Suggested by Michael Friendly.)

  A data frame with 48 observations on the following 14 variables. There
  are 3 factors and 9 response variables.

  `Group`
      a factor with 12 levels, corresponding to the combinations of
      `Contour` and `Depth`

  `Contour`
      a factor with 3 levels: `Depression` `Slope` `Top`

  `Depth`
      a factor with 4 levels: `0-10` `10-30` `30-60` `60-90`

  `Gp`
      a factor with 12 levels, giving abbreviations for the groups: `D0`
      `D1` `D3` `D6` `S0` `S1` `S3` `S6` `T0` `T1`
      `T3` `T6`

  `Block`
      a factor with levels `1` `2` `3` `4`

  `pH`
      soil pH

  `N`
      total nitrogen in %

  `Dens`
      bulk density in gm/cm$^3$

  `P`
      total phosphorous in ppm

  `Ca`
      calcium in me/100 gm.

  `Mg`
      magnesium in me/100 gm.

  `K`
      phosphorous in me/100 gm.

  `Na`
      sodium in me/100 gm.

  `Conduc`
      conductivity

  Horton, I. F.,Russell, J. S., and Moore, A. W. (1968)
  Multivariate-covariance and canonical analysis: A method for selecting
  the most effective discriminators in a multivariate situation.
  *Biometrics* **24**, 845–858. Originally from
  http://www.stat.lsu.edu/faculty/moser/exst7037/soils.sas but no longer
  available there.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `soils.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'soils.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Soils.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='soils.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
