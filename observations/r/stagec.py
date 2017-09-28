# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def stagec(path):
  """Stage C Prostate Cancer

  A set of 146 patients with stage C prostate cancer, from a study
  exploring the prognostic value of flow cytometry.

  A data frame with 146 observations on the following 8 variables.

  `pgtime`
      Time to progression or last follow-up (years)

  `pgstat`
      1 = progression observed, 0 = censored

  `age`
      age in years

  `eet`
      early endocrine therapy, 1 = no, 2 = yes

  `g2`
      percent of cells in G2 phase, as found by flow cytometry

  `grade`
      grade of the tumor, Farrow system

  `gleason`
      grade of the tumor, Gleason system

  `ploidy`
      the ploidy status of the tumor, from flow cytometry. Values are
      diploid, tetraploid, and aneuploid

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `stagec.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 146 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'stagec.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/rpart/stagec.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='stagec.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
