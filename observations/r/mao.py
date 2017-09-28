# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mao(path):
  """A study of Parkinson's disease and MAO gene

  The markers are both with actual allele sizes and allele numbers. The
  dataset is distributed with the GENECOUNTING version 2.0 illustrating
  gene counting method involving chromosome X. A total of 183 patients and
  157 controls (150 males, 190 females) were available, together with five
  markers in MAOA (monoamine oxidase A) region with alleles 12, 9, 6, 5,
  3, and the first three markers were genotyped in all individuals while
  the fourth and fifth were genotyped for 294 and 304 individuals.

  A data frame

  Dr Helen Latsoudis of Institute of Psychiatry, KCL

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mao.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 340 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mao.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/mao.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mao.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
