# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nass_cds(path):
  """Airbag and other influences on accident fatalities

  US data, for 1997-2002, from police-reported car crashes in which there
  is a harmful event (people or property), and from which at least one
  vehicle was towed. Data are restricted to front-seat occupants, include
  only a subset of the variables recorded, and are restricted in other
  ways also.

  A data frame with 26217 observations on the following 15 variables.

  `dvcat`
      ordered factor with levels (estimated impact speeds) `1-9km/h`,
      `10-24`, `25-39`, `40-54`, `55+`

  `weight`
      Observation weights, albeit of uncertain accuracy, designed to
      account for varying sampling probabilities.

  `dead`
      factor with levels `alive` `dead`

  `airbag`
      a factor with levels `none` `airbag`

  `seatbelt`
      a factor with levels `none` `belted`

  `frontal`
      a numeric vector; 0 = non-frontal, 1=frontal impact

  `sex`
      a factor with levels `f` `m`

  `ageOFocc`
      age of occupant in years

  `yearacc`
      year of accident

  `yearVeh`
      Year of model of vehicle; a numeric vector

  `abcat`
      Did one or more (driver or passenger) airbag(s) deploy? This factor
      has levels `deploy` `nodeploy` `unavail`

  `occRole`
      a factor with levels `driver` `pass`

  `deploy`
      a numeric vector: 0 if an airbag was unavailable or did not deploy;
      1 if one or more bags deployed.

  `injSeverity`
      a numeric vector; 0:none, 1:possible injury, 2:no incapacity,
      3:incapacity, 4:killed; 5:unknown, 6:prior death

  `caseid`
      character, created by pasting together the populations sampling
      unit, the case number, and the vehicle number. Within each year, use
      this to uniquely identify the vehicle.

  http://www.stat.colostate.edu/~meyer/airbags.htm\\
  ftp://ftp.nhtsa.dot.gov/nass/

  See also\\ http://www.maths.anu.edu.au/~johnm/datasets/airbags

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nass_cds.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26217 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nass_cds.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nassCDS.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nass_cds.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
