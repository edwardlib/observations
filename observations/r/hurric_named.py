# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hurric_named(path):
  """Named US Atlantic Hurricanes

  Details are given of atmospheric pressure at landfall, estimated damage
  in millions of dollars, and deaths, for named hurricanes that made
  landfall in the US mainland from 1950 through to 2012.

  A data frame with 94 observations on the following 11 variables.

  `Name`
      Hurricane name

  `Year`
      Numeric

  `LF.WindsMPH`
      Maximum sustained windspeed (>= 1 minute) to occur along the US
      coast. Prior to 1980, this is estimated from the maximum windspeed
      associated with the Saffir-Simpson index at landfall. If 2 or more
      landfalls, the maximum is taken

  `LF.PressureMB`
      Atmospheric pressure at landfall in millibars. If 2 or more
      landfalls, the minimum is taken

  `LF.times`
      Date of first landfall

  `BaseDam2014`
      Property damage (millions of 2014 US dollars)

  `BaseDamage`
      Property damage (in millions of dollars for that year)

  `NDAM2014`
      Damage, had hurricane appeared in 2014

  `AffectedStates`
      Affected states (2-digit abbreviations), pasted together

  `firstLF`
      Date of first landfall

  `deaths`
      Number of continental US direct and indirect deaths

  `mf`
      Gender of name; a factor with levels `f` `m`

  http://www.icatdamageestimator.com/ Deaths except for Audrey and
  Katrina, are in the Excel file that is available from
  http://www.pnas.org/content/suppl/2014/05/30/1402786111.DCSupplemental
  NOAA Monthly Weather Reports (MWRs) supplied the numbers of deaths for
  all except Donna, Celia, Audrey and Katrina. The figure for Celia is
  from http://www.nhc.noaa.gov/pdf/NWS-TPC-5.pdf. For the other three
  hurricanes it is from the Atlantic hurricane list in Wikipedia (see the
  references.)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hurric_named.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 94 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hurric_named.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/hurricNamed.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hurric_named.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
