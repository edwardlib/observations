# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nuts(path):
  """nuts

  Squirrel data set (nuts) from Zuur, Hilbe, and Ieno (2013). As
  originally reported by Flaherty et al (2012), researchers recorded
  information about squirrel behavior and forest attributes across various
  plots in Scotland's Abernathy Forest. The study focused on the following
  variables. response cones number of cones stripped by red squirrels per
  plot predictor sntrees standardized number of trees per plot sheight
  standardized mean tree height per plot scover standardized percentage of
  canopy cover per plot The stripped cone count was only taken when the
  mean diameter of trees was under 0.6m (dbh).

  A data frame with 52 observations on the following 8 variables.

  `cones`
      number cones stripped by squirrels

  `ntrees`
      number of trees per plot

  `dbh`
      number DBH per plot

  `height`
      mean tree height per plot

  `cover`
      canopy closure (as a percentage)

  `sntrees`
      standardized number of trees per plot

  `sheight`
      standardized mean tree height per plot

  `scover`
      standardized canopy closure (as a percentage)

  Zuur, Hilbe, Ieno (2013), A Beginner's Guide to GLM and GLMM using R,
  Highlands

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nuts.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 52 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nuts.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/nuts.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nuts.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
