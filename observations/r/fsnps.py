# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fsnps(path):
  """A case-control data involving four SNPs with missing genotype

  This is a simulated data of four SNPs with their alleles coded in
  characters. The variable y contains phenotypes (1=case, 0=control).

  A data frame


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fsnps.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 432 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fsnps.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/fsnps.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fsnps.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
