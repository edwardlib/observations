# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def infmrt(path):
  """infmrt

  Data loads lazily. Type data(infmrt) into the console.

  A data.frame with 102 rows and 12 variables:

  -  year. 1987 or 1990

  -  infmort. deaths per 1,000 live births

  -  afdcprt. afdc partic., 1000s

  -  popul. population, 1000s

  -  pcinc. per capita income

  -  physic. drs. per 100,000 civilian pop.

  -  afdcper. percent on AFDC

  -  d90. =1 if year == 1990

  -  lpcinc. log(pcinc)

  -  lphysic. log(physic)

  -  DC. =1 for Washington DC

  -  lpopul. log(popul)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `infmrt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 102 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'infmrt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/infmrt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='infmrt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
