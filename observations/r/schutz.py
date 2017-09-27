# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def schutz(path):
  """The Schutz correlation matrix example from Shapiro and ten Berge

  Shapiro and ten Berge use the Schutz correlation matrix as an example
  for Minimum Rank Factor Analysis. The Schutz data set is also a nice
  example of how normal minres or maximum likelihood will lead to a
  Heywood case, but minrank factoring will not.

  The format is: num [1:9, 1:9] 1 0.8 0.28 0.29 0.41 0.38 0.44 0.4 0.41
  0.8 ... - attr(\*, "dimnames")=List of 2 ..$ :1] "Word meaning" "Odd
  Words" "Boots" "Hatchets" ... ..$ : chr [1:9] "V1" "V2" "V3" "V4" ...

  Richard E. Schutz,(1958) Factorial Validity of the Holzinger-Crowdeer
  Uni-factor tests. Educational and Psychological Measurement, 48,
  873-875.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `schutz.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'schutz.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Schutz.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='schutz.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
