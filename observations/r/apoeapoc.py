# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def apoeapoc(path):
  """APOE/APOC1 markers and Alzheimer's

  This data set contains APOE/APOC1 markers and Chinese Alzheimer's
  patients and controls. Variable id is subject id and y takes value 0 for
  controls and 2 for Alzheimer's.

  The last six variables are age, sex and genotypes for APOE and APOC with
  suffixes for each of two alleles (".a1" and ".a2").

  A data frame

  Shi J, Zhang S, Ma C, Liu X, Li T, Tang M, Han H, Guo Y, Zhao JH, Zheng
  K, Kong X, Zhang K, Su Z, Zhao Z. Association between apolipoprotein CI
  HpaI polymorphism and sporadic Alzheimer's disease in Chinese. Acta

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `apoeapoc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 353 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'apoeapoc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/apoeapoc.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='apoeapoc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
