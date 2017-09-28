# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def marriage(path):
  """Marriage records

  Marriage records from the Mobile County, Alabama, probate court.

  A data frame with 98 observations on the following variables.

  -  `bookpageID` a factor with levels for each book and page (unique
     identifier)

  -  `appdate` a factor with levels corresponding to each of the dates
     on which the application was filed (in the form MO/DY/YY, e.g.
     1/22/99 represents January 22, 1999)

  -  `ceremonydate` a factor with levels corresponding to the date of
     the ceremony

  -  `delay` number of days between the application and the ceremony

  -  `officialTitle` a factor with levels `BISHOP` `CATHOLIC PRIEST`
     `CHIEF CLERK` `CIRCUIT JUDGE ` `ELDER` `MARRIAGE OFFICIAL`
     `MINISTER` `PASTOR` `REVEREND`

  -  `person` a factor with levels `Bride` `Groom`

  -  `dob` a factor with levels corresponding to the date of birth of
     the person

  -  `age` age of the person (in years)

  -  `race` a factor with levels `American Indian` `Black`
     `Hispanic` `White`

  -  `prevcount` the number of previous marriages of the person, as
     listed on the application

  -  `prevconc` the way the last marriage ended, as listed on the
     application

  -  `hs` the number of years of high school education, as listed on the
     application

  -  `college` the number of years College education, as listed on the
     application. Where no number was listed, this field was left blank,
     unless less than 12 years High School was reported, in which case it
     was entered as 0.

  -  `dayOfBirth` the day of birth, as a number from 1 to 365 counting
     from January 1

  -  `sign` the astrological sign, with levels `Aquarius` `Aries`
     `Cancer` `Capricorn` `Gemini` `Leo` `Libra` `Pisces`
     `Saggitarius` `Scorpio` `Taurus` `Virgo`

  The records were collected through
  http://www.mobilecounty.org/probatecourt/recordssearch.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `marriage.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 98 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'marriage.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Marriage.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='marriage.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
