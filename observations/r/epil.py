# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def epil(path):
  """Seizure Counts for Epileptics

  Thall and Vail (1990) give a data set on two-week seizure counts for 59
  epileptics. The number of seizures was recorded for a baseline period of
  8 weeks, and then patients were randomly assigned to a treatment group
  or a control group. Counts were then recorded for four successive
  two-week periods. The subject's age is the only covariate.

  This data frame has 236 rows and the following 9 columns:

  `y`
      the count for the 2-week period.

  `trt`
      treatment, `"placebo"` or `"progabide"`.

  `base`
      the counts in the baseline 8-week period.

  `age`
      subject's age, in years.

  `V4`
      `0/1` indicator variable of period 4.

  `subject`
      subject number, 1 to 59.

  `period`
      period, 1 to 4.

  `lbase`
      log-counts for the baseline period, centred to have zero mean.

  `lage`
      log-ages, centred to have zero mean.

  Thall, P. F. and Vail, S. C. (1990) Some covariance models for
  longitudinal count data with over-dispersion. *Biometrics* **46**,
  657–671.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `epil.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 236 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'epil.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/epil.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='epil.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
