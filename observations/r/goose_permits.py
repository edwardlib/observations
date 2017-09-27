# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def goose_permits(path):
  """Goose Permit Study

  237 hunters were each offered one of 11 cash amounts (bids) ranging from
  $1 to $200 in return for their goose permits. Hunters returned either
  their permit or the cash.

  A data.frame with 11 observations on the following 3 variables.

  itemcodebid amount offered for permit (US $) [numeric] itemcodekeep
  number of hunters who kept the permit and returned the cash [numeric]
  itemcodesell number of hunters who kept the cash and returned the permit
  [numeric]

  Bishop and Heberlein. "Measuring values of extramarket goods: are
  indirect measures biased?". Amer. J. Agr. Econ. 61, 1979. Available at
  http://www1.udel.edu/johnmack/frec343/bishop_and_heberlein.pdf. See also
  http://www.math.umt.edu/patterson/ProfileLikelihoodCI.pdf.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `goose_permits.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'goose_permits.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/GoosePermits.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='goose_permits.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
