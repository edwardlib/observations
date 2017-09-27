# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hmda(path):
  """The Boston HMDA Data Set

  a cross-section from 1997-1998

  *number of observations* : 2381 *observation* : individuals *country* :
  United States

  In package version 0.2-9 and earlier this dataset was called Hdma.

  A dataframe containing :

  dir
      debt payments to total income ratio

  hir
      housing expenses to income ratio

  lvr
      ratio of size of loan to assessed value of property

  ccs
      consumer credit score from 1 to 6 (a low value being a good score)

  mcs
      mortgage credit score from 1 to 4 (a low value being a good score)

  pbcr
      public bad credit record ?

  dmi
      denied mortgage insurance ?

  self
      self employed ?

  single
      is the applicant single ?

  uria
      1989 Massachusetts unemployment rate in the applicant's industry

  condominium
      is unit a condominium ? (was called comdominiom in version 0.2-9 and
      earlier versions of the package)

  black
      is the applicant black ?

  deny
      mortgage application denied ?

  Federal Reserve Bank of Boston.

  Munnell, Alicia H., Geoffrey M.B. Tootell, Lynne E. Browne and James
  McEneaney (1996) “Mortgage lending in Boston: Interpreting HMDA data”,
  *American Economic Review*, 25-53.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hmda.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2381 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hmda.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Hmda.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hmda.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
