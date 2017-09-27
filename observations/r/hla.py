# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hla(path):
  """The HLA data

  This data set contains HLA markers DRB, DQA, DQB and phenotypes of 271
  Schizophrenia patients (y=1) and controls (y=0). Genotypes for 3 HLA
  loci have prefixes name (e.g., "DQB") and a suffix for each of two
  alleles (".a1" and ".a2").

  A data frame containing 271 rows and 8 columns


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hla.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 271 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hla.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/hla.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hla.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
