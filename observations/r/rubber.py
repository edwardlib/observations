# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rubber(path):
  """Accelerated Testing of Tyre Rubber

  Data frame from accelerated testing of tyre rubber.

  `loss`
      the abrasion loss in gm/hr.

  `hard`
      the hardness in Shore units.

  `tens`
      tensile strength in kg/sq m.

  O.L. Davies (1947) *Statistical Methods in Research and Production.*
  Oliver and Boyd, Table 6.1 p. 119.

  O.L. Davies and P.L. Goldsmith (1972) *Statistical Methods in Research
  and Production.* 4th edition, Longmans, Table 8.1 p. 239.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rubber.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rubber.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Rubber.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rubber.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
