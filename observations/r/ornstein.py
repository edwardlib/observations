# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ornstein(path):
  """Interlocking Directorates Among Major Canadian Firms

  The `Ornstein` data frame has 248 rows and 4 columns. The observations
  are the 248 largest Canadian firms with publicly available information
  in the mid-1970s. The names of the firms were not available.

  This data frame contains the following columns:

  assets
      Assets in millions of dollars.

  sector
      Industrial sector. A factor with levels: `AGR`, agriculture, food,
      light industry; `BNK`, banking; `CON`, construction; `FIN`,
      other financial; `HLD`, holding companies; `MAN`, heavy
      manufacturing; `MER`, merchandizing; `MIN`, mining, metals,
      etc.; `TRN`, transport; `WOD`, wood and paper.

  nation
      Nation of control. A factor with levels: `CAN`, Canada; `OTH`,
      other foreign; `UK`, Britain; `US`, United States.

  interlocks
      Number of interlocking director and executive positions shared with
      other major firms.

  Ornstein, M. (1976) The boards and executives of the largest Canadian
  corporations. *Canadian Journal of Sociology* **1**, 411–437.

  Personal communication from M. Ornstein, Department of Sociology, York
  University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ornstein.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 248 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ornstein.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Ornstein.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ornstein.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
