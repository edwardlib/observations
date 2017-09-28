# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aldh2(path):
  """ALDH2 markers and Alcoholism

  This data set contains eight ALDH2 markers and Japanese alcohlic
  patients (y=1) and controls (y=0). There are genotypes for 8 loci, with
  a prefix name (e.g., "EXON12") and a suffix for each of two alleles
  (".a1" and ".a2").

  The eight markers loci follows the following map (base pairs)

  +------------+------------------+
  | D12S2070   | (> 450 000),     |
  +------------+------------------+
  | D12S839    | (> 450 000),     |
  +------------+------------------+
  | D12S821    | (*~* 400 000),   |
  +------------+------------------+
  | D12S1344   | ( 83 853),       |
  +------------+------------------+
  | EXON12     | ( 0),            |
  +------------+------------------+
  | EXON1      | ( 37 335),       |
  +------------+------------------+
  | D12S2263   | ( 38 927),       |
  +------------+------------------+
  | D12S1341   | (> 450 000)      |
  +------------+------------------+

  A data frame

  Prof Ian Craig of Oxford and SGDP Centre, KCL

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aldh2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 263 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aldh2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/aldh2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aldh2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
