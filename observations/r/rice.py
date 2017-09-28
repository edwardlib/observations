# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rice(path):
  """Genetically Modified and Wild Type Rice Data

  The `rice` data frame has 72 rows and 7 columns. The data are from an
  experiment that compared wild type (wt) and genetically modified rice
  plants (ANU843), each with three different chemical treatments (F10,
  NH4Cl, and NH4NO3).

  This data frame contains the following columns:

  PlantNo
      a numeric vector

  Block
      a numeric vector

  RootDryMass
      a numeric vector

  ShootDryMass
      a numeric vector

  trt
      a factor with levels `F10`, `NH4Cl`, `NH4NO3`,
      `F10 +ANU843`, `NH4Cl +ANU843`, `NH4NO3 +ANU843`

  fert
      a factor with levels `F10` `NH4Cl` `NH4NO3`

  variety
      a factor with levels `wt` `ANU843`

  Perrine, F.M., Prayitno, J., Weinman, J.J., Dazzo, F.B. and Rolfe, B.
  2001. Rhizobium plasmids are involved in the inhibition or stimulation
  of rice growth and development. Australian Journal of Plant Physiology
  28: 923-927.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rice.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rice.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/rice.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rice.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
