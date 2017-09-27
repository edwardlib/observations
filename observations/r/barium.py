# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def barium(path):
  """barium

  Data loads lazily. Type data(barium) into the console.

  A data.frame with 131 rows and 31 variables:

  -  chnimp. Chinese imports, bar. chl.

  -  bchlimp. total imports bar. chl.

  -  befile6. =1 for all 6 mos before filing

  -  affile6. =1 for all 6 mos after filing

  -  afdec6. =1 for all 6 mos after decision

  -  befile12. =1 all 12 mos before filing

  -  affile12. =1 all 12 mos after filing

  -  afdec12. =1 all 12 mos after decision

  -  chempi. chemical production index

  -  gas. gasoline production

  -  rtwex. exchange rate index

  -  spr. =1 for spring months

  -  sum. =1 for summer months

  -  fall. =1 for fall months

  -  lchnimp. log(chnimp)

  -  lgas. log(gas)

  -  lrtwex. log(rtwex)

  -  lchempi. log(chempi)

  -  t. time trend

  -  feb. =1 if month is feb

  -  mar. =1 if month is march

  -  apr.

  -  may.

  -  jun.

  -  jul.

  -  aug.

  -  sep.

  -  oct.

  -  nov.

  -  dec.

  -  percchn. percent imports from china

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `barium.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 131 rows and 31 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'barium.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/barium.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='barium.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
