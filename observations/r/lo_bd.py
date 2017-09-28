# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lo_bd(path):
  """Cancer drug data use to provide an example of the use of the skew power di
  stributions.

  A portion of an experiment to determine the limit of blank/limit of
  detection in a biochemical assay.

  A data frame with 84 observations on the following 9 variables.

  `pool`
      a factor with levels `1` `2` `3` `4` `5` `6` `7` `8`
      `9` `10` `11` `12` denoting the 12 pools used in the
      experiment; each pool had a different level of drug.

  `I1L1`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I1L2`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I2L1`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I2L2`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I3L1`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I3L2`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I4L1`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  `I4L2`
      a numeric vector giving the measured concentration in pmol/L of drug
      in the assay

  Used as an illustrative example for Box-Cox type transformations with
  negative readings in Hawkins and Weisberg (2015). For examples of its
  use, see `skewPower`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lo_bd.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 84 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lo_bd.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/LoBD.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lo_bd.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
