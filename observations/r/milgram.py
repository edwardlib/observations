# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def milgram(path):
  """Milgram

  Attitudes towards ethics of a famous Milgram experiment

  A dataset with 37 observations on the following 2 variables.

  `Results`

  Treatment group: `Actual`, `Complied`, or `Refused`

  `Score`

  Ethical score from 1 (not at all ethical) to 9 (completely ethical)

  "An experimental study of attitudes toward deception" by Mary Ann
  DiMatteo. Unpublished manuscript, Department of Psychology and Social

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `milgram.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'milgram.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Milgram.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='milgram.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
