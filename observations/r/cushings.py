# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cushings(path):
  """Diagnostic Tests on Patients with Cushing's Syndrome

  Cushing's syndrome is a hypertensive disorder associated with
  over-secretion of cortisol by the adrenal gland. The observations are
  urinary excretion rates of two steroid metabolites.

  The `Cushings` data frame has 27 rows and 3 columns:

  `Tetrahydrocortisone`
      urinary excretion rate (mg/24hr) of Tetrahydrocortisone.

  `Pregnanetriol`
      urinary excretion rate (mg/24hr) of Pregnanetriol.

  `Type`
      underlying type of syndrome, coded `a` (adenoma) , `b`
      (bilateral hyperplasia), `c` (carcinoma) or `u` for unknown.

  J. Aitchison and I. R. Dunsmore (1975) *Statistical Prediction
  Analysis.* Cambridge University Press, Tables 11.1–3.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cushings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cushings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Cushings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cushings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
