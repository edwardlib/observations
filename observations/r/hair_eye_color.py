from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hair_eye_color(path):
  """Hair and Eye Color of Statistics Students

  Distribution of hair and eye color and sex in 592 statistics students.

  A 3-dimensional array resulting from cross-tabulating 592 observations
  on 3 variables. The variables and their levels are as follows:

  +------+--------+-----------------------------+
  | No   | Name   | Levels                      |
  +------+--------+-----------------------------+
  | 1    | Hair   | Black, Brown, Red, Blond    |
  +------+--------+-----------------------------+
  | 2    | Eye    | Brown, Blue, Hazel, Green   |
  +------+--------+-----------------------------+
  | 3    | Sex    | Male, Female                |
  +------+--------+-----------------------------+

  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/haireye.sas

  Snee (1974) gives the two-way table aggregated over `Sex`. The `Sex`
  split of the ‘Brown hair, Brown eye’ cell was changed to agree with that
  used by Friendly (2000).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hair_eye_color.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hair_eye_color.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/datasets/HairEyeColor.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hair_eye_color.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
