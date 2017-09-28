# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hawks(path):
  """Hawks

  Data for a sample of hawks

  A dataset with 908 observations on the following 19 variables.

  `Month`

  code8=September to `12`\ =December

  `Day`

  Date in the month

  `Year`

  Year: 1992-2003

  `CaptureTime`

  Time of capture (HH:MM)

  `ReleaseTime`

  Time of release (HH:MM)

  `BandNumber`

  ID band code

  `Species`

  `CH`\ =Cooper's, `RT`\ =Red-tailed, `SS`\ =Sharp-Shinned

  `Age`

  `A`\ =Adult or `I`\ =Imature

  `Sex`

  `F`\ =Female or `M`\ =Male

  `Wing`

  Length (in mm) of primary wing feather from tip to wrist it attaches to

  `Weight`

  Body weight (in gm)

  `Culmen`

  Length (in mm) of the upper bill from the tip to where it bumps into the
  fleshy part of the bird

  `Hallux`

  Length (in mm) of the killing talon

  `Tail`

  Measurement (in mm) related to the length of the tail (invented at the
  MacBride Raptor Center)

  `StandardTail`

  Standared measurement of tail length (in mm)

  `Tarsus`

  Length of the basic foot bone (in mm)

  `WingPitFat`

  Amount of fat in the wing pit

  `KeelFat`

  Amount of fat on the breastbone (measured by feel

  `Crop`

  Amount of material in the crop, coded from `1`\ =full to `0`\ =empty

  Many thanks to the late Professor Bob Black at Cornell College for

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hawks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 908 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hawks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Hawks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hawks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
