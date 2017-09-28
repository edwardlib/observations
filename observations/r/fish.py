# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fish(path):
  """fish

  Data loads lazily. Type data(fish) into the console.

  A data.frame with 97 rows and 20 variables:

  -  prca. price for Asian buyers

  -  prcw. price for white buyers

  -  qtya. quantity sold to Asians

  -  qtyw. quantity sold to whites

  -  mon. =1 if Monday

  -  tues. =1 if Tuesday

  -  wed. =1 if Wednesday

  -  thurs. =1 if Thursday

  -  speed2. min past 2 days wind speeds

  -  wave2. avg max last 2 days wave height

  -  speed3. 3 day lagged max windspeed

  -  wave3. avg max wave hghts of 3 & 4 day lagged hghts

  -  avgprc. ((prca\*qtya) + (prcw\*qtyw))/(qtya + qtyw)

  -  totqty. qtya + qtyw

  -  lavgprc. log(avgprc)

  -  ltotqty. log(totqty)

  -  t. time trend

  -  lavgp\_1. lavgprc[\_n-1]

  -  gavgprc. lavgprc - lavgp\_1

  -  gavgp\_1. gavgprc[\_n-1]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fish.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 97 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fish.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/fish.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fish.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
