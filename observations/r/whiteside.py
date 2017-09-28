# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def whiteside(path):
  """House Insulation: Whiteside's Data

  Mr Derek Whiteside of the UK Building Research Station recorded the
  weekly gas consumption and average external temperature at his own house
  in south-east England for two heating seasons, one of 26 weeks before,
  and one of 30 weeks after cavity-wall insulation was installed. The
  object of the exercise was to assess the effect of the insulation on gas
  consumption.

  The `whiteside` data frame has 56 rows and 3 columns.:

  `Insul`
      A factor, before or after insulation.

  `Temp`
      Purportedly the average outside temperature in degrees Celsius.
      (These values is far too low for any 56-week period in the 1960s in
      South-East England. It might be the weekly average of daily minima.)

  `Gas`
      The weekly gas consumption in 1000s of cubic feet.

  A data set collected in the 1960s by Mr Derek Whiteside of the UK
  Building Research Station. Reported by

  Hand, D. J., Daly, F., McConway, K., Lunn, D. and Ostrowski, E. eds
  (1993) *A Handbook of Small Data Sets.* Chapman & Hall, p. 69.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `whiteside.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'whiteside.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/whiteside.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='whiteside.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
