# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fars(path):
  """US fatal road accident data for automobiles, 1998 to 2010

  Data are from the US FARS (Fatality Analysis Recording System) archive
  that is intended to include every accident in which there was at least
  one fatality. Data are limited to vehicles where the front seat
  passenger seat was occupied.

  A data frame with 153338 observations on the following 17 variables.

  `caseid`
      a character vector: identifies the vehicle

  `state`
      a numeric vector. See the FARS website for details

  `age`
      a numeric vector; 998=not reported; 999=not known

  `airbag`
      a numeric vector

  `injury`
      a numeric vector

  `restraint`
      a numeric vector

  `sex`
      1=male, 2=female, 9=unknown

  `inimpact`
      a numeric vector

  `modelyr`
      a numeric vector

  `airbagAvail`
      a factor with levels `no` `yes` `NA-code`

  `airbagDeploy`
      a factor with levels `no` `yes` `NA-code`

  `Restraint`
      a factor with levels `no` `yes` `NA-code`

  `D_injury`
      a numeric vector

  `D_airbagAvail`
      a factor with levels `no` `yes` `NA-code`

  `D_airbagDeploy`
      a factor with levels `no` `yes` `NA-code`

  `D_Restraint`
      a factor with levels `no` `yes` `NA-code`

  `year`
      year of accident

  Details
  ~~~~~~~

  Data is for automabiles where the right passenger seat was occupied,
  with one observation for each such passenger. Observations for vehicles
  where the most harmful event was a fire or explosion or immersion or gas
  inhalation, or where someone fell or jumped from the vehicle, are
  omitted. Data are limited to vehicle body types 1 to 19,48,49,61, or 62.
  This excludes large trucks, pickup trucks, vans and buses. The 2009 and
  2010 data does not include information on whether airbags were
  installed.

  http://www-fars.nhtsa.dot.gov/Main/index.aspx

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 151158 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gamclass/FARS.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
