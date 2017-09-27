# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def insurance(path):
  """Numbers of Car Insurance claims

  The data given in data frame `Insurance` consist of the numbers of
  policyholders of an insurance company who were exposed to risk, and the
  numbers of car insurance claims made by those policyholders in the third
  quarter of 1973.

  This data frame contains the following columns:

  `District`
      factor: district of residence of policyholder (1 to 4): 4 is major
      cities.

  `Group`
      an ordered factor: group of car with levels <1 litre, 1–1.5 litre,
      1.5–2 litre, >2 litre.

  `Age`
      an ordered factor: the age of the insured in 4 groups labelled <25,
      25–29, 30–35, >35.

  `Holders`
      numbers of policyholders.

  `Claims`
      numbers of claims

  L. A. Baxter, S. M. Coutts and G. A. F. Ross (1980) Applications of
  linear models in motor insurance. *Proceedings of the 21st International
  Congress of Actuaries, Zurich* pp. 11–29.

  M. Aitkin, D. Anderson, B. Francis and J. Hinde (1989) *Statistical
  Modelling in GLIM.* Oxford University Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `insurance.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 64 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'insurance.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Insurance.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='insurance.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
