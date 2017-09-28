# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nep499(path):
  """A study of Alzheimer's disease with eight SNPs and APOE

  This is a study of the neprilysin gene and sporadic Alzheimer's disease
  in Chinese. There are 257 cases and 242 controls, each with eight SNPs
  detecting through denaturing high-performance liquid chromatography
  (DHPLC).

  A data frame

  Shi J, Zhang S, Tang M, Ma C, Zhao J, Li T, Liu X, Sun Y, Guo Y, Han H,
  Ma Y, Zhao Z. Mutation Screening and Association Study of the Neprilysin
  Gene in Sporadic Alzheimer's Disease in Chinese Persons. J Gerontol A:

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nep499.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 499 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nep499.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/nep499.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nep499.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
