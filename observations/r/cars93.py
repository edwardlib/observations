# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cars93(path):
  """Data from 93 Cars on Sale in the USA in 1993

  The `Cars93` data frame has 93 rows and 27 columns.

  This data frame contains the following columns:

  `Manufacturer`
      Manufacturer.

  `Model`
      Model.

  `Type`
      Type: a factor with levels `"Small"`, `"Sporty"`, `"Compact"`,
      `"Midsize"`, `"Large"` and `"Van"`.

  `Min.Price`
      Minimum Price (in \\$1,000): price for a basic version.

  `Price`
      Midrange Price (in \\$1,000): average of `Min.Price` and
      `Max.Price`.

  `Max.Price`
      Maximum Price (in \\$1,000): price for “a premium version”.

  `MPG.city`
      City MPG (miles per US gallon by EPA rating).

  `MPG.highway`
      Highway MPG.

  `AirBags`
      Air Bags standard. Factor: none, driver only, or driver & passenger.

  `DriveTrain`
      Drive train type: rear wheel, front wheel or 4WD; (factor).

  `Cylinders`
      Number of cylinders (missing for Mazda RX-7, which has a rotary
      engine).

  `EngineSize`
      Engine size (litres).

  `Horsepower`
      Horsepower (maximum).

  `RPM`
      RPM (revs per minute at maximum horsepower).

  `Rev.per.mile`
      Engine revolutions per mile (in highest gear).

  `Man.trans.avail`
      Is a manual transmission version available? (yes or no, Factor).

  `Fuel.tank.capacity`
      Fuel tank capacity (US gallons).

  `Passengers`
      Passenger capacity (persons)

  `Length`
      Length (inches).

  `Wheelbase`
      Wheelbase (inches).

  `Width`
      Width (inches).

  `Turn.circle`
      U-turn space (feet).

  `Rear.seat.room`
      Rear seat room (inches) (missing for 2-seater vehicles).

  `Luggage.room`
      Luggage capacity (cubic feet) (missing for vans).

  `Weight`
      Weight (pounds).

  `Origin`
      Of non-USA or USA company origins? (factor).

  `Make`
      Combination of Manufacturer and Model (character).

  Lock, R. H. (1993) 1993 New Car Data. *Journal of Statistics Education*
  **1**\ (1).
  http://www.amstat.org/publications/jse/v1n1/datasets.lock.html.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cars93.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 93 rows and 27 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cars93.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Cars93.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cars93.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
