# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lowbrth(path):
  """lowbrth

  Data loads lazily. Type data(lowbrth) into the console.

  A data.frame with 100 rows and 36 variables:

  -  year. 1987 or 1990

  -  lowbrth. perc births low weight

  -  infmort. infant mortality rate

  -  afdcprt. # participants in AFDC, 1000s

  -  popul. population, 1000s

  -  pcinc. per capita income

  -  physic. # physicians, 1000s

  -  afdcprc. percent of pop in AFDC

  -  d90. =1 if year == 1990

  -  lpcinc. log of pcinc

  -  cafdcprc. change in afdcprc

  -  clpcinc. change in lpcinc

  -  lphysic. log of physic

  -  clphysic. change in lphysic

  -  clowbrth. change in lowbrth

  -  cinfmort. change in infmort

  -  afdcpay. avg monthly AFDC payment

  -  afdcinc. afdcpay as percent pcinc

  -  lafdcpay. log of afdcpay

  -  clafdcpy. change in lafdcpay

  -  cafdcinc. change in afdcinc

  -  stateabb. state postal code

  -  state. name of state

  -  beds. # hospital beds, 1000s

  -  bedspc. beds per capita

  -  lbedspc. log(bedspc)

  -  clbedspc. change in lbedspc

  -  povrate. percent people below poverty line

  -  cpovrate. change in povrate

  -  afdcpsq. afdcper^2

  -  cafdcpsq. change in afdcpsq

  -  physicpc. physicians per capita

  -  lphypc. log(physicpc)

  -  clphypc. change in lphypc

  -  lpopul. log(popul)

  -  clpopul. change in lpopul

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lowbrth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 36 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lowbrth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/lowbrth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lowbrth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
