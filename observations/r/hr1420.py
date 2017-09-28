# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hr1420(path):
  """An example data for Manhattan plot with annotation

  This example contains p values for a list of SNPs wtih information on
  chromosome, position and gene symnol.

  In the reference below, seven established SNPs are in light blue, 14 new
  SNPs in dark blue and those failed to replicate in red. The paper size
  is set to 189 width x 189/2 height (mm) and 1200 dpi resolution. The
  font is Verdana. See `mhtplot2` for all the details.

  A data frame

  Dr Marcel den Hoed at the MRC Epidemiology Unit

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hr1420.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 147849 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hr1420.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/hr1420.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hr1420.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
