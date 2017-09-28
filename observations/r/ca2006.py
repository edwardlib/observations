# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ca2006(path):
  """California Congressional Districts in 2006

  Election returns and identifying information, California's 53
  congressional districts in the 2006 Congresisonal elections.

  A data frame with 53 observations on the following 11 variables.

  `district`
      numeric, number of Congressional district

  `D`
      numeric, number of votes for the Democratic candidate

  `R`
      numeric, votes for the Republican candidate

  `Other`
      numeric, votes for other candidates

  `IncParty`
      character, party of the incumbent (or retiring member), `D` or
      `R`

  `IncName`
      character, last name of the incumbent, character `NA` if no
      incumbent running

  `open`
      logical, `TRUE` if no incumbent running

  `contested`
      logical, `TRUE` if both major parties ran candidates

  `Bush2004`
      numeric, votes for George W. Bush (R) in the district in the 2004
      presidential election

  `Kerry2004`
      numeric, votes for John Kerry (D) in 2004

  `Other2004`
      numeric votes for other candidates in 2004

  `Bush2000`
      numeric, votes for George W. Bush in 2000

  `Gore2000`
      numeric, votes for Al Gore (D) in 2000

  2006 data from the California Secretary of State's web site,
  http://vote2006.sos.ca.gov/Returns/usrep/all.htm. 2004 and 2000
  presidential vote in congressional districts from the 2006 *Almanac of
  American Politics*.

  Thanks to Arthur Aguirre for the updated links, above.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ca2006.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 53 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ca2006.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/ca2006.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ca2006.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
