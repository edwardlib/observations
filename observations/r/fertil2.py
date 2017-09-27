# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fertil2(path):
  """fertil2

  Data loads lazily. Type data(fertil2) into the console.

  A data.frame with 4361 rows and 27 variables:

  -  mnthborn. month woman born

  -  yearborn. year woman born

  -  age. age in years

  -  electric. =1 if has electricity

  -  radio. =1 if has radio

  -  tv. =1 if has tv

  -  bicycle. =1 if has bicycle

  -  educ. years of education

  -  ceb. children ever born

  -  agefbrth. age at first birth

  -  children. number of living children

  -  knowmeth. =1 if know about birth control

  -  usemeth. =1 if ever use birth control

  -  monthfm. month of first marriage

  -  yearfm. year of first marriage

  -  agefm. age at first marriage

  -  idlnchld. 'ideal' number of children

  -  heduc. husband's years of education

  -  agesq. age^2

  -  urban. =1 if live in urban area

  -  urb\_educ. urban\*educ

  -  spirit. =1 if religion == spirit

  -  protest. =1 if religion == protestant

  -  catholic. =1 if religion == catholic

  -  frsthalf. =1 if mnthborn <= 6

  -  educ0. =1 if educ == 0

  -  evermarr. =1 if ever married

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fertil2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4361 rows and 27 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fertil2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/fertil2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fertil2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
