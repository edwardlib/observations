# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def p_erisk(path):
  """Political Economic Risk Data from 62 Countries in 1987

  Political Economic Risk Data from 62 Countries in 1987.

  A data frame with 62 observations on the following 6 variables. All data
  points are from 1987. See Quinn (2004) for more details.

  country: a factor with levels 'Argentina' 'Australia' 'Austria'
  'Bangladesh' 'Belgium' 'Bolivia' 'Botswana' 'Brazil' 'Burma' 'Cameroon'
  'Canada' 'Chile' 'Colombia' 'Congo-Kinshasa' 'Costa Rica' 'Cote
  d'Ivoire' 'Denmark' 'Dominican Republic' 'Ecuador' 'Finland' 'Gambia,
  The' 'Ghana' 'Greece' 'Hungary' 'India' 'Indonesia' 'Iran' 'Ireland'
  'Israel' 'Italy' 'Japan' 'Kenya' 'Korea, South' 'Malawi' 'Malaysia'
  'Mexico' 'Morocco' 'New Zealand' 'Nigeria' 'Norway' 'Papua New Guinea'
  'Paraguay' 'Philippines' 'Poland' 'Portugal' 'Sierra Leone' 'Singapore'
  'South Africa' 'Spain' 'Sri Lanka' 'Sweden' 'Switzerland' 'Syria'
  'Thailand' 'Togo' 'Tunisia' 'Turkey' 'United Kingdom' 'Uruguay'
  'Venezuela' 'Zambia' 'Zimbabwe'

  courts: an ordered factor with levels '0' < '1'.'courts' is an indicator
  of whether the country in question is judged to have an independent
  judiciary. From Henisz (2002).

  barb2: a numeric vector giving the natural log of the black market
  premium in each country. The black market premium is coded as the black
  market exchange rate (local currency per dollar) divided by the official
  exchange rate minus 1. From Marshall, Gurr, and Harff (2002).

  prsexp2: an ordered factor with levels '0' < '1' < '2' < '3' < '4' <
  '5', giving the lack of expropriation risk. From Marshall, Gurr, and
  Harff (2002).

  prscorr2: an ordered factor with levels '0' < '1' < '2' < '3' < '4' <
  '5', measuring the lack of corruption. From Marshall, Gurr, and Harff
  (2002).

  gdpw2: a numeric vector giving the natural log of real GDP per worker in
  1985 international prices. From Alvarez et al. (1999).

  Mike Alvarez, Jose Antonio Cheibub, Fernando Limongi, and Adam
  Przeworski. 1999. “ACLP Political and Economic Database.” <URL:
  http://www.ssc.upenn.edu/~cheibub/data/>.

  Witold J. Henisz. 2002. “The Political Constraint Index (POLCON)
  Dataset.” \\ <URL:
  http://www-management.wharton.upenn.edu/henisz/POLCON/ContactInfo.
  html>.

  Monty G. Marshall, Ted Robert Gurr, and Barbara Harff. 2002. “State
  Failure Task Force Problem Set.” <URL:
  http://www.cidcm.umd.edu/inscr/stfail/index.htm>.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `p_erisk.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'p_erisk.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/PErisk.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='p_erisk.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
