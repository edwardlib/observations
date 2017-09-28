# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wage1(path):
  """wage1

  Data loads lazily. Type data(wage1) into the console.

  A data.frame with 526 rows and 24 variables:

  -  wage. average hourly earnings

  -  educ. years of education

  -  exper. years potential experience

  -  tenure. years with current employer

  -  nonwhite. =1 if nonwhite

  -  female. =1 if female

  -  married. =1 if married

  -  numdep. number of dependents

  -  smsa. =1 if live in SMSA

  -  northcen. =1 if live in north central U.S

  -  south. =1 if live in southern region

  -  west. =1 if live in western region

  -  construc. =1 if work in construc. indus.

  -  ndurman. =1 if in nondur. manuf. indus.

  -  trcommpu. =1 if in trans, commun, pub ut

  -  trade. =1 if in wholesale or retail

  -  services. =1 if in services indus.

  -  profserv. =1 if in prof. serv. indus.

  -  profocc. =1 if in profess. occupation

  -  clerocc. =1 if in clerical occupation

  -  servocc. =1 if in service occupation

  -  lwage. log(wage)

  -  expersq. exper^2

  -  tenursq. tenure^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wage1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 526 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wage1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/wage1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wage1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
