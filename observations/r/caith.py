# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def caith(path):
  """Colours of Eyes and Hair of People in Caithness

  Data on the cross-classification of people in Caithness, Scotland, by
  eye and hair colour. The region of the UK is particularly interesting as
  there is a mixture of people of Nordic, Celtic and Anglo-Saxon origin.

  A 4 by 5 table with rows the eye colours (blue, light, medium, dark) and
  columns the hair colours (fair, red, medium, dark, black).

  Fisher, R.A. (1940) The precision of discriminant functions. *Annals of
  Eugenics (London)* **10**, 422–429.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `caith.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'caith.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/caith.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='caith.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
