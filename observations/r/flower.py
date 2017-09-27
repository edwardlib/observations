# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def flower(path):
  """Flower Characteristics

  8 characteristics for 18 popular flowers.

  A data frame with 18 observations on 8 variables:

  +-------------+-----------+--------------+
  | [ , "V1"]   | factor    | winters      |
  +-------------+-----------+--------------+
  | [ , "V2"]   | factor    | shadow       |
  +-------------+-----------+--------------+
  | [ , "V3"]   | factor    | tubers       |
  +-------------+-----------+--------------+
  | [ , "V4"]   | factor    | color        |
  +-------------+-----------+--------------+
  | [ , "V5"]   | ordered   | soil         |
  +-------------+-----------+--------------+
  | [ , "V6"]   | ordered   | preference   |
  +-------------+-----------+--------------+
  | [ , "V7"]   | numeric   | height       |
  +-------------+-----------+--------------+
  | [ , "V8"]   | numeric   | distance     |
  +-------------+-----------+--------------+

  V1
      winters, is binary and indicates whether the plant may be left in
      the garden when it freezes.

  V2
      shadow, is binary and shows whether the plant needs to stand in the
      shadow.

  V3
      tubers, is asymmetric binary and distinguishes between plants with
      tubers and plants that grow in any other way.

  V4
      color, is nominal and specifies the flower's color (1 = white, 2 =
      yellow, 3 = pink, 4 = red, 5 = blue).

  V5
      soil, is ordinal and indicates whether the plant grows in dry (1),
      normal (2), or wet (3) soil.

  V6
      preference, is ordinal and gives someone's preference ranking going
      from 1 to 18.

  V7
      height, is interval scaled, the plant's height in centimeters.

  V8
      distance, is interval scaled, the distance in centimeters that
      should be left between the plants.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `flower.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'flower.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/flower.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='flower.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
