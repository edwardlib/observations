# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fishing1(path):
  """Choice of Fishing Mode

  a cross-section

  *number of observations* : 1182

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  mode
      recreation mode choice, on of : beach, pier, boat and charter

  price
      price for chosen alternative

  catch
      catch rate for chosen alternative

  pbeach
      price for beach mode

  ppier
      price for pier mode

  pboat
      price for private boat mode

  pcharter
      price for charter boat mode

  cbeach
      catch rate for beach mode

  cpier
      catch rate for pier mode

  cboat
      catch rate for private boat mode

  ccharter
      catch rate for charter boat mode

  income
      monthly income

  Herriges, J. A. and C. L. Kling (1999) “Nonlinear Income Effects in
  Random Utility Models”, *Review of Economics and Statistics*, **81**,
  62-72.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fishing1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1182 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fishing1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Fishing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fishing1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
