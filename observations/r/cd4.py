# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cd4(path):
  """CD4 Counts for HIV-Positive Patients

  The `cd4` data frame has 20 rows and 2 columns.

  CD4 cells are carried in the blood as part of the human immune system.
  One of the effects of the HIV virus is that these cells die. The count
  of CD4 cells is used in determining the onset of full-blown AIDS in a
  patient. In this study of the effectiveness of a new anti-viral drug on
  HIV, 20 HIV-positive patients had their CD4 counts recorded and then
  were put on a course of treatment with this drug. After using the drug
  for one year, their CD4 counts were again recorded. The aim of the
  experiment was to show that patients taking the drug had increased CD4
  counts which is not generally seen in HIV-positive patients.

  This data frame contains the following columns:

  `baseline`
      The CD4 counts (in 100's) on admission to the trial.

  `oneyear `
      The CD4 counts (in 100's) after one year of treatment with the new
      drug.

  The data were obtained from

  DiCiccio, T.J. and Efron B. (1996) Bootstrap confidence intervals (with
  Discussion). *Statistical Science*, **11**, 189–228.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cd4.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cd4.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/cd4.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cd4.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
