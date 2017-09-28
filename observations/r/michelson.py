# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def michelson(path):
  """Michelson's Determinations of the Velocity of Light

  The data frame `Michelson` gives Albert Michelson's measurements of
  the velocity of light in air, made from June 5 to July 2, 1879, reported
  in Michelson (1882). The given values + 299,000 are Michelson's
  measurements in km/sec. The number of cases is 100 and the "true" value
  on this scale is 734.5.

  Stigler (1977) used these data to illustrate properties of robust
  estimators with real, historical data. For this purpose, he divided the
  100 measurements into 5 sets of 20 each. These are contained in
  `MichelsonSets`.

  `Michelson`: A data frame with 100 observations on the following
  variable, given in time order of data collection

  `velocity`
      a numeric vector

  `MichelsonSets`: A 20 x 5 matrix, with format int [1:20, 1:5] 850 850
  1000 810 960 800 830 830 880 720 ... - attr(\*, "dimnames")=List of 2
  ..$ : NULL ..$ : chr [1:5] "ds12" "ds13" "ds14" "ds15" ...

  Kyle Siegrist, "Virtual Laboratories in Probability and Statistics",
  http://www.math.uah.edu/stat/data/Michelson.html

  Stephen M. Stigler (1977), "Do robust estimators work with *real*
  data?", *Annals of Statistics*, 5, 1055-1098

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `michelson.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'michelson.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Michelson.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='michelson.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
