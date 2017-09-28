# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_state_abbrev(path):
  """Standard abbreviations for states of the United States

  The object returned by `readUSstateAbbreviations()` on May 20, 2013.

  A `data.frame` containing 10 different character vectors of names or
  codes for 76 different political entities including the United States,
  the 50 states within the US, plus the District of Columbia, US
  territories and other political designation, some of which are obsolete
  but are included for historical reference.

  Name
      The standard name of the entity.

  Status
      description of status, e.g., state / commonwealth vs. island,
      territory, military mail code, etc.

  ISO, ANSI.letters, ANSI.digits, USPS, USCG, Old.GPO, AP, Other
      Alternative abbreviations used per different standards. The most
      commonly used among these may be the 2-letter codes officially used
      by the US Postal Service (`USPS`).

  `the Wikipedia article on "List of U.S. state
abbreviations" <http://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations
  >`__

  See Also
  ~~~~~~~~

  `readUSstateAbbreviations` `showNonASCII`
  `grepNonStandardCharacters` `subNonStandardCharacters`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_state_abbrev.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 76 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_state_abbrev.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/USstateAbbreviations.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_state_abbrev.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
