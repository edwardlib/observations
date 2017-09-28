# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rareplants(path):
  """Rare and Endangered Plant Species

  These data were taken from species lists for South Australia, Victoria
  and Tasmania. Species were classified as CC, CR, RC and RR, with C
  denoting common and R denoting rare. The first code relates to South
  Australia and Victoria, and the second to Tasmania. They were further
  classified by habitat according to the Victorian register, where D = dry
  only, W = wet only, and WD = wet or dry.

  The format is: chr "rareplants"

  Jasmyn Lynch, Department of Botany and Zoology at Australian National
  University

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rareplants.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rareplants.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/rareplants.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rareplants.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
