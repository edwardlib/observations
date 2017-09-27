# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def clouds(path):
  """Cloud Seeding Data

  Data from an experiment investigating the use of massive amounts of
  silver iodide (100 to 1000 grams per cloud) in cloud seeding to increase
  rainfall.

  A data frame with 24 observations on the following 7 variables.

  seeding
      a factor indicating whether seeding action occured (`no` or
      `yes`).

  time
      number of days after the first day of the experiment.

  sne
      suitability criterion.

  cloudcover
      the percentage cloud cover in the experimental area, measured using
      radar.

  prewetness
      the total rainfall in the target area one hour before seeding (in
      cubic metres times `1e+8`).

  echomotion
      a factor showing whether the radar echo was `moving` or
      `stationary`.

  rainfall
      the amount of rain in cubic metres times `1e+8`.

  W. L. Woodley, J. Simpson, R. Biondini and J. Berkeley (1977), Rainfall
  results 1970-75: Florida area cumulus experiment. *Science* **195**,
  735–742.

  R. D. Cook and S. Weisberg (1980), Characterizations of an empirical
  influence function for detecting influential cases in regression.
  *Technometrics* **22**, 495–508.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `clouds.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'clouds.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/clouds.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='clouds.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
