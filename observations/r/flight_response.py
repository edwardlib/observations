# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def flight_response(path):
  """FlightResponse

  Flight Response of Pacific Brant

  A dataset with 464 observations on the following 7 variables.

  `FlockID`

  Flock ID

  `Altitude`

  Altitude of the overflight by the helicopter (in 100m)

  `Lateral`

  Lateral distance (in 100m) between the aircraft and flock

  `Flight`

  `1`\ =more than 10% of flock flies away or `0`\ =otherwise

  `AltLat`

  Product of Altitude x Lateral

  `AltCat`

  Altitude categories: `low`\ =under 3, `mid`\ =3 to 6,
  `high`\ =over 6

  `LatCat`

  Lateral categories: `1`\ under 10 to `4`\ =over 30

  Data come from the book Statistical Case Studies: A Collaboration
  Between Academe and Industry, Roxy Peck, Larry D. Haugh, and Arnold

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `flight_response.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 464 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'flight_response.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FlightResponse.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='flight_response.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
