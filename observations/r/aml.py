# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aml(path):
  """Remission Times for Acute Myelogenous Leukaemia

  The `aml` data frame has 23 rows and 3 columns.

  A clinical trial to evaluate the efficacy of maintenance chemotherapy
  for acute myelogenous leukaemia was conducted by Embury et al. (1977) at
  Stanford University. After reaching a stage of remission through
  treatment by chemotherapy, patients were randomized into two groups. The
  first group received maintenance chemotherapy and the second group did
  not. The aim of the study was to see if maintenance chemotherapy
  increased the length of the remission. The data here formed a
  preliminary analysis which was conducted in October 1974.

  This data frame contains the following columns:

  `time`
      The length of the complete remission (in weeks).

  `cens`
      An indicator of right censoring. 1 indicates that the patient had a
      relapse and so `time` is the length of the remission. 0 indicates
      that the patient had left the study or was still in remission in
      October 1974, that is the length of remission is right-censored.

  `group`
      The group into which the patient was randomized. Group 1 received
      maintenance chemotherapy, group 2 did not.

  The data were obtained from

  Miller, R.G. (1981) *Survival Analysis*. John Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aml.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aml.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/aml.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aml.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
