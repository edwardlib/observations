# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def watervoles(path):
  """Water Voles Data

  Percentage incidence of the 13 characteristics of water voles in 14
  areas.

  A dissimilarity matrix for the following 14 variables, i.e, areas:
  `Surrey`, `Shropshire`, `Yorkshire`, `Perthshire`, `Aberdeen`,
  `Elean Gamhna`, `Alps`, `Yugoslavia`, `Germany`, `Norway`,
  `Pyrenees I`, `Pyrenees II`, `North Spain`, and `South Spain`.

  G. B. Corbet, J. Cummins, S. R. Hedges, W. J. Krzanowski (1970), The
  taxonomic structure of British water voles, genus *Arvicola*. *Journal
  of Zoology*, **61**, 301–316.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `watervoles.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'watervoles.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/watervoles.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='watervoles.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
