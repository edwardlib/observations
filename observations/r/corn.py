# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def corn(path):
  """corn

  Data loads lazily. Type data(corn) into the console.

  A data.frame with 37 rows and 5 variables:

  -  county. county number

  -  cornhec. corn per hectare

  -  soyhec. soybeans per hectare

  -  cornpix. corn pixels per hectare

  -  soypix. soy pixels per hectare

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `corn.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'corn.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/wooldridge/corn.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='corn.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
