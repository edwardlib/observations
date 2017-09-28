# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mhtdata(path):
  """An example data for Manhattan plot

  This example contains p values for a list of SNPs whose information
  regarding chromosome, position and reference seqeuence as with gene
  annotation is obtained separately.

  A data frame

  Dr Tuomas Kilpelainen at the MRC Epidemiology Unit

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mhtdata.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 159312 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mhtdata.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/mhtdata.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mhtdata.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
