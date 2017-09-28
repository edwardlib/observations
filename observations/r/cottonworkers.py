# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cottonworkers(path):
  """Occupation and wage profiles of British cotton workers

  Numbers are given in different categories of worker, in each of two
  investigations. The first source of information is the Board of Trade
  Census that was conducted on 1886. The second is a relatively informal
  survey conducted by US Bureau of Labor representatives in 1889, for use
  in official reports.

  A data frame with 14 observations on the following 3 variables.

  census1886
      Numbers of workers in each of 14 different categories, according to
      the Board of Trade wage census that was conducted in 1886

  survey1889
      Numbers of workers in each of 14 different categories, according to
      data collected in 1889 by the US Bureau of Labor, for use in a
      report to the US Congress and House of Representatives

  avwage
      Average wage, in pence, as estimated in the US Bureau of Labor
      survey

  United States congress, House of Representatives, Sixth Annual Report of
  the Commissioner of Labor, 1890, Part III, Cost of Living (Washington
  D.C. 1891); idem., Seventh Annual Report of the Commissioner of Labor,
  1891, Part III, Cost of Living (Washington D.C. 1892)

  Return of wages in the principal textile trades of the United Kingdom,
  with report therein. (P.P. 1889, LXX). United Kingdom Official
  Publication.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cottonworkers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cottonworkers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/cottonworkers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cottonworkers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
