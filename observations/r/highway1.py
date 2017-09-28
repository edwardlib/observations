# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def highway1(path):
  """Highway Accidents

  The data comes from a unpublished master's paper by Carl Hoffstedt. They
  relate the automobile accident rate, in accidents per million vehicle
  miles to several potential terms. The data include 39 sections of large
  highways in the state of Minnesota in 1973. The goal of this analysis
  was to understand the impact of design variables, `Acpts`, `Slim`,
  `Sig`, and `Shld` that are under the control of the highway
  department, on accidents.

  This data frame contains the following columns:

  rate
      1973 accident rate per million vehicle miles

  len
      length of the `Highway1` segment in miles

  adt
      average daily traffic count in thousands

  trks
      truck volume as a percent of the total volume

  sigs1
      (number of signalized interchanges per mile times len + 1)/len, the
      number of signals per mile of roadway, adjusted to have no zero
      values.

  slim
      speed limit in 1973

  shld
      width in feet of outer shoulder on the roadway

  lane
      total number of lanes of traffic

  acpt
      number of access points per mile

  itg
      number of freeway-type interchanges per mile

  lwid
      lane width, in feet

  htype
      An indicator of the type of roadway or the source of funding for the
      road, either MC, FAI, PA, or MA

  Carl Hoffstedt. This differs from the dataset `Highway` in the
  `alr4` package only by addition of transformation of some of the
  columns.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `highway1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 39 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'highway1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Highway1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='highway1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
