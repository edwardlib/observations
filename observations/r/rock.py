# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rock(path):
  """Measurements on Petroleum Rock Samples

  Measurements on 48 rock samples from a petroleum reservoir.

  A data frame with 48 rows and 4 numeric columns.

  +--------+---------+----------------------------------------------------+
  | [,1]   | area    | area of pores space, in pixels out of 256 by 256   |
  +--------+---------+----------------------------------------------------+
  | [,2]   | peri    | perimeter in pixels                                |
  +--------+---------+----------------------------------------------------+
  | [,3]   | shape   | perimeter/sqrt(area)                               |
  +--------+---------+----------------------------------------------------+
  | [,4]   | perm    | permeability in milli-Darcies                      |
  +--------+---------+----------------------------------------------------+


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rock.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rock.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/rock.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rock.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
