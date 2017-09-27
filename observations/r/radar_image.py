# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def radar_image(path):
  """Satellite Radar Image Data from near Munich

  The data were supplied by A. Frery. They are a part of a synthetic
  aperture satellite radar image corresponding to a suburb of Munich.
  Provided are coordinates and values corresponding to three frequency
  bands for each of 1573 pixels.

  A data frame with 1573 observations on the following 5 variables.

  `X.coord`
      a numeric vector

  `Y.coord`
      a numeric vector

  `Band.1`
      a numeric vector

  `Band.2`
      a numeric vector

  `Band.3`
      a numeric vector

  The website accompanying the MMY-book:
  http://www.wiley.com/legacy/wileychi/robust_statistics

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `radar_image.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1573 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'radar_image.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/radarImage.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='radar_image.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
