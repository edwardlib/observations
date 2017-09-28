# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def arbuthnot(path):
  """Arbuthnot's data on male and female birth ratios in London from 1629-1710.

  John Arbuthnot (1710) used these time series data on the ratios of male
  to female births in London from 1629-1710 to carry out the first known
  significance test, comparing observed data to a null hypothesis. The
  data for these 81 years showed that in every year there were more male
  than female christenings.

  On the assumption that male and female births were equally likely, he
  showed that the probability of observing 82 years with more males than
  females was vanishingly small (*~ 4.14 x 10^{-25}*). He used this to
  argue that a nearly constant birth ratio > 1 could be interpreted to
  show the guiding hand of a devine being. The data set adds variables of
  deaths from the plague and total mortality obtained by Campbell and from
  Creighton (1965).

  A data frame with 82 observations on the following 7 variables.

  `Year`
      a numeric vector, 1629-1710

  `Males`
      a numeric vector, number of male christenings

  `Females`
      a numeric vector, number of female christenings

  `Plague`
      a numeric vector, number of deaths from plague

  `Mortality`
      a numeric vector, total mortality

  `Ratio`
      a numeric vector, ratio of Males/Females

  `Total`
      a numeric vector, total christenings in London (000s)

  Arbuthnot, John (1710). "An argument for Devine Providence, taken from
  the constant Regularity observ'd in the Births of both Sexes,"
  *Philosophical transactions*, 27, 186-190. Published in 1711.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `arbuthnot.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 82 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'arbuthnot.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Arbuthnot.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='arbuthnot.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
