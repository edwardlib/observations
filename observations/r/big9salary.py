# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def big9salary(path):
  """big9salary

  Data loads lazily. Type data(big9salary) into the console.

  A data.frame with 786 rows and 30 variables:

  -  id. person identifier

  -  year. 92, 95, or 99

  -  salary. annual salary, $

  -  pubindx. publication index

  -  totpge. standardized total article pages

  -  assist. =1 if assistant professor

  -  assoc. =1 if associate professor

  -  prof. =1 if full professor

  -  chair. =1 if department chair

  -  top20phd. =1 if Ph.D. from top 20 dept.

  -  yearphd. year Ph.D. obtained

  -  female. =1 if female

  -  osu. =1 if Ohio State U.

  -  iowa. =1 if U. Iowa

  -  indiana. =1 if Indiana U.

  -  purdue. =1 if Purdue U.

  -  msu. =1 if Michigan State U.

  -  minn. =1 if U. Minnesota

  -  mich. =1 if U. Michigan

  -  wisc. =1 if U. Wisconsin

  -  illinois. =1 if U. Illinois

  -  y92. =1 if year == 92

  -  y95. =1 if year == 95

  -  y99. =1 if year == 99

  -  lsalary. log(salary)

  -  exper. years since first teaching job

  -  expersq. exper^2

  -  pubindxsq. pubindx^2

  -  pubindx0. =1 if pubindx == 0

  -  lpubindx. log(pubindx) if pubindx > 0

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `big9salary.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 786 rows and 30 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'big9salary.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/big9salary.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='big9salary.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
