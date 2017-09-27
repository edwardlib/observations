# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def prison(path):
  """prison

  Data loads lazily. Type data(prison) into the console.

  A data.frame with 714 rows and 45 variables:

  -  state. alphabetical; DC = 9

  -  year. 80 to 93

  -  govelec. =1 if gubernatorial election

  -  black. proportion black

  -  metro. proportion in metro. areas

  -  unem. proportion unemployed

  -  criv. viol. crimes per 100,000

  -  crip. prop. crimes per 100,000

  -  lcriv. log(criv)

  -  lcrip. log(crip)

  -  gcriv. lcriv - lcriv\_1

  -  gcrip. lcrip - lcrip\_1

  -  y81. =1 if year == 81

  -  y82.

  -  y83.

  -  y84.

  -  y85.

  -  y86.

  -  y87.

  -  y88.

  -  y89.

  -  y90.

  -  y91.

  -  y92.

  -  y93.

  -  ag0\_14. prop. pop. 0 to 14 yrs

  -  ag15\_17. prop. pop. 15 to 17 yrs

  -  ag18\_24. prop. pop. 18 to 24 yrs

  -  ag25\_34. prop. pop. 25 to 34 yrs

  -  incpc. per capita income, nominal

  -  polpc. police per 100,000 residents

  -  gincpc. log(incpc) - log(incpc\_1)

  -  gpolpc. lpolpc - lpolpc\_1

  -  cag0\_14. change in ag0\_14

  -  cag15\_17. change in ag15\_17

  -  cag18\_24. change in ag18\_24

  -  cag25\_34. change in ag25\_34

  -  cunem. change in unem

  -  cblack. change in black

  -  cmetro. change in metro

  -  pris. prison pop. per 100,000

  -  lpris. log(pris)

  -  gpris. lpris - lpris[\_n-1]

  -  final1. =1 if fnl dec on litig, curr yr

  -  final2. =1 if dec on litig, prev 2 yrs

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `prison.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 714 rows and 45 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'prison.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/prison.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='prison.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
