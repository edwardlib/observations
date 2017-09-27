# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cran_packages(path):
  """Growth of CRAN

  Data casually collected on the number of packages on the Comprehensive R
  Archive Network (CRAN) at different dates.

  NOTE: This could change in the future. See Details below.

  A `data.frame` containing:

  Version
      an ordered factor of the R version number primarily in use at the
      time. This was taken from archives of the major releases at
    https://svn.r-project.org/R/branches/R-1-3-patches/tests/internet.Rout.sa
  ve,
      ...
    https://svn.r-project.org/R/branches/R-3-1-branch/tests/internet.Rout.sav
  e

  Date
      an object of class `Date` giving the date on which the count of
      the number of CRAN packages was determined.

  Packages
      an integer number of packages on the CRAN mirror checked on the
      indicated `Date`.

  Source
      A factor giving the source (person) who collected the data.

  John Fox, "Aspects of the Social Organization and Trajectory of the R
  Project", *R Journal*, 1(2), Dec. 2009, 5-13.
  https://journal.r-project.org/archive/2009-2/RJournal_2009-2_Fox.pdf,
  accessed 2014-04-13.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cran_packages.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 29 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cran_packages.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/CRANpackages.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cran_packages.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
