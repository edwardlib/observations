# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fringe(path):
  """fringe

  Data loads lazily. Type data(fringe) into the console.

  A data.frame with 616 rows and 39 variables:

  -  annearn. annual earnings, $

  -  hrearn. hourly earnings, $

  -  exper. years work experience

  -  age. age in years

  -  depends. number of dependents

  -  married. =1 if married

  -  tenure. years with current employer

  -  educ. years schooling

  -  nrtheast. =1 if live in northeast

  -  nrthcen. =1 if live in north central

  -  south. =1 if live in south

  -  male. =1 if male

  -  white. =1 if white

  -  union. =1 if union member

  -  office.

  -  annhrs. annual hours worked

  -  ind1. industry dummy

  -  ind2.

  -  ind3.

  -  ind4.

  -  ind5.

  -  ind6.

  -  ind7.

  -  ind8.

  -  ind9.

  -  vacdays. $ value of vac. days

  -  sicklve. $ value of sick leave

  -  insur. $ value of employee insur

  -  pension. $ value of employee pension

  -  annbens. vacdays+sicklve+insur+pension

  -  hrbens. hourly benefits, $

  -  annhrssq. annhrs^2

  -  beratio. annbens/annearn

  -  lannhrs. log(annhrs)

  -  tenuresq. tenure^2

  -  expersq. exper^2

  -  lannearn. log(annearn)

  -  peratio. pension/annearn

  -  vserat. (vacdays+sicklve)/annearn

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fringe.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 616 rows and 39 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fringe.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/fringe.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fringe.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
