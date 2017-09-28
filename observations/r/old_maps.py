# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def old_maps(path):
  """Latitudes and Longitudes of 39 Points in 11 Old Maps

  The data set is concerned with the problem of aligning the coordinates
  of points read from old maps (1688 - 1818) of the Great Lakes area. 39
  easily identifiable points were selected in the Great Lakes area, and
  their (lat, long) coordinates were recorded using a grid overlaid on
  each of 11 old maps, and using linear interpolation.

  It was conjectured that maps might be systematically in error in five
  key ways: (a) constant error in latitude; (b)constant error in
  longitude; (c) proportional error in latitude; (d)proportional error in
  longitude; (e) angular error from a non-zero difference between true
  North and the map's North.

  One challenge from these data is to produce useful analyses and
  graphical displays that relate to these characteristics or to other
  aspects of the data.

  A data frame with 468 observations on the following 6 variables, giving
  the latitude and longitude of 39 points recorded from 12 sources (Actual
  + 11 maps).

  `point`
      a numeric vector

  `col`
      Column in the table a numeric vector

  `name`
      Name of the map maker, using `Actual` for the true coordinates of
      the points. A factor with levels `Actual` `Arrowsmith` `Belin`
      `Cary` `Coronelli` `D'Anville} \code{Del'Isle` `Lattre`
      `Melish` `Mitchell` `Popple`

  `year`
      Year of the map

  `lat`
      Latitude

  `long`
      Longitude

  Andrews, D. F., and Herzberg, A. M. (1985). *Data: A Collection of
  Problems from Many fields for the Student and Research Worker*. New
  York: Springer, Table 10.1. The data were obtained from
  http://www.stat.duke.edu/courses/Spring01/sta114/data/Andrews/T10.1.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `old_maps.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 468 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'old_maps.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/OldMaps.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='old_maps.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
