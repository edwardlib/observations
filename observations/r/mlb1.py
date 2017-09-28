# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mlb1(path):
  """mlb1

  Data loads lazily. Type data(mlb1) into the console.

  A data.frame with 353 rows and 47 variables:

  -  salary. 1993 season salary

  -  teamsal. team payroll

  -  nl. =1 if national league

  -  years. years in major leagues

  -  games. career games played

  -  atbats. career at bats

  -  runs. career runs scored

  -  hits. career hits

  -  doubles. career doubles

  -  triples. career triples

  -  hruns. career home runs

  -  rbis. career runs batted in

  -  bavg. career batting average

  -  bb. career walks

  -  so. career strike outs

  -  sbases. career stolen bases

  -  fldperc. career fielding perc

  -  frstbase. = 1 if first base

  -  scndbase. =1 if second base

  -  shrtstop. =1 if shortstop

  -  thrdbase. =1 if third base

  -  outfield. =1 if outfield

  -  catcher. =1 if catcher

  -  yrsallst. years as all-star

  -  hispan. =1 if hispanic

  -  black. =1 if black

  -  whitepop. white pop. in city

  -  blackpop. black pop. in city

  -  hisppop. hispanic pop. in city

  -  pcinc. city per capita income

  -  gamesyr. games per year in league

  -  hrunsyr. home runs per year

  -  atbatsyr. at bats per year

  -  allstar. perc. of years an all-star

  -  slugavg. career slugging average

  -  rbisyr. rbis per year

  -  sbasesyr. stolen bases per year

  -  runsyr. runs scored per year

  -  percwhte. percent white in city

  -  percblck. percent black in city

  -  perchisp. percent hispanic in city

  -  blckpb. black\*percblck

  -  hispph. hispan\*perchisp

  -  whtepw. white\*percwhte

  -  blckph. black\*perchisp

  -  hisppb. hispan\*percblck

  -  lsalary. log(salary)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mlb1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 353 rows and 47 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mlb1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/mlb1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mlb1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
