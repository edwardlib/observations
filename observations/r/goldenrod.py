# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def goldenrod(path):
  """Goldenrod Galls

  Measurements for a sample of goldenrod galls

  A dataset with 1055 observations on the following 9 variables.

  `Gdiam03`

  Gall diameter in 2003 (in mm)

  `Stdiam03`

  Stem diameter in 2003 (in mm)

  `Wall03`

  Wall thickness in 2003 (in mm)

  `Fate03`

  `b`\ =beetle present `e`\ =early death `f`\ =living fly larva
  `g`\ =living wasp `o`\ =pupal case `u`\ =unknown

  `Gdiam04`

  Gall diameter in 2004 (in mm)

  `Stdiam04`

  Stem diameter in 2004 (in mm)

  `Wall04`

  Wall thickness in 2003 (in mm)

  `Fate04`

  `b`\ =beetle present `e`\ =early death `f`\ =living fly larva
  `g`\ =living wasp `o`\ =pupal case `u`\ =unknown

  `Fly04`

  Fly in 2004? `n` or `y`

  Thanks to the Kenyon College Department of Biology for sharing these

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `goldenrod.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1055 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'goldenrod.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Goldenrod.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='goldenrod.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
