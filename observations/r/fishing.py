# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fishing(path):
  """fishing

  The fishing data is adapted from Zuur, Hilbe and Ieno (2013) to
  determine whether the data appears to be generated from more than one
  generating mechanism. The data are originally adapted from Bailey et al.
  (2008) who were interested in how certain deep-sea fish populations were
  impacted when commercial fishing began in locations with deeper water
  than in previous years. Given that there are 147 sites that were
  researched, the model is of (1) the total number of fish counted per
  site (totabund); ( 2) on the mean water depth per site (meandepth); (3)
  adjusted by the area of the site (sweptarea); (4) the log of which is
  the model offset.

  A data frame with 147 observations on the following variables.

  `totabund`
      total fish counted per site

  `meandepth`
      mean water depth per site

  `sweptarea`
      adjusted area of site

  `density`
      folage density index

  `site`
      catch site

  `year`
      1977-2002

  `period`
      0=1977-1989; 1=2000+

  Zuur, Hilbe, Ieno (2013), A Beginner's Guide to GLM and GLMM using R,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fishing.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 147 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fishing.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/fishing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fishing.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
