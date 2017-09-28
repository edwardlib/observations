# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sexual_fun(path):
  """Sex is Fun

  Data from Hout et al. (1987) given by Agresti (1990) summarizing the
  responses of married couples to the questionnaire item: Sex is fun for
  me and my partner: (a) never or occasionally, (b) fairly often, (c) very
  often, (d) almost always.

  A 2-dimensional array resulting from cross-tabulating the ratings of 91
  married couples. The variables and their levels are as follows:

  +------+-----------+---------------------------------------------------+
  | No   | Name      | Levels                                            |
  +------+-----------+---------------------------------------------------+
  | 1    | Husband   | Never Fun, Fairly Often, Very Often, Always Fun   |
  +------+-----------+---------------------------------------------------+
  | 2    | Wife      | Never Fun, Fairly Often, Very Often, Always Fun   |
  +------+-----------+---------------------------------------------------+

  M. Friendly (2000), Visualizing Categorical Data, page 91.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sexual_fun.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sexual_fun.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/SexualFun.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sexual_fun.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
