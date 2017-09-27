# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def blot(path):
  """Bond's Logical Operations Test – BLOT

  35 items for 150 subjects from Bond's Logical Operations Test. A good
  example of Item Response Theory analysis using the Rasch model. One
  parameter (Rasch) analysis and two parameter IRT analyses produce
  somewhat different results.

  A data frame with 150 observations on 35 variables. The BLOT was
  developed as a paper and pencil test for children to measure Logical
  Thinking as discussed by Piaget and Inhelder.

  The data are taken (with kind permission from Trevor Bond) from the
  webpage http://homes.jcu.edu.au/~edtgb/book/data/Bond87.txt and read
  using read.fwf.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `blot.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 150 rows and 35 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'blot.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/blot.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='blot.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
