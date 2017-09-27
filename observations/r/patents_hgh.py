# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def patents_hgh(path):
  """Dynamic Relation Between Patents and R\\&D

  a panel of 346 observations from 1975 to 1979

  *number of observations* : 1730

  *observation* : production units

  *country* : United States

  A dataframe containing :

  obsno
      firm index

  year
      year

  cusip
      Compustat's identifying number for the firm (Committee on Uniform
      Security Identification Procedures number)

  ardsic
      a two-digit code for the applied R&D industrial classification
      (roughly that in Bound, Cummins, Griliches, Hall, and Jaffe, in the
      Griliches R&D, Patents, and Productivity volume)

  scisect
      is the firm in the scientific sector ?

  logk
      the logarithm of the book value of capital in 1972.

  sumpat
      the sum of patents applied for between 1972-1979.

  logr
      the logarithm of R&D spending during the year (in 1972 dollars)

  logr1
      the logarithm of R&D spending (one year lag)

  logr2
      the logarithm of R&D spending (two years lag)

  logr3
      the logarithm of R&D spending (three years lag)

  logr4
      the logarithm of R&D spending (four years lag)

  logr5
      the logarithm of R&D spending (five years lag)

  pat
      the number of patents applied for during the year that were
      eventually granted

  pat1
      the number of patents (one year lag)

  pat2
      the number of patents (two years lag)

  pat3
      the number of patents (three years lag)

  pat4
      the number of patents (four years lag)

  Hall, Bronwyn , Zvi Griliches and Jerry Hausman (1986) “Patents and R&D:
  Is There a Lag?”, *International Economic Review*, **27**, 265-283.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `patents_hgh.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1730 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'patents_hgh.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/PatentsHGH.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='patents_hgh.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
