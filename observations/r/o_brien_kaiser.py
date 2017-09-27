# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def o_brien_kaiser(path):
  """O'Brien and Kaiser's Repeated-Measures Data

  These contrived repeated-measures data are taken from O'Brien and Kaiser
  (1985). The data are from an imaginary study in which 16 female and male
  subjects, who are divided into three treatments, are measured at a
  pretest, postest, and a follow-up session; during each session, they are
  measured at five occasions at intervals of one hour. The design,
  therefore, has two between-subject and two within-subject factors.

  The contrasts for the `treatment` factor are set to *-2, 1, 1* and *0,
  -1, 1*. The contrasts for the `gender` factor are set to
  `contr.sum`.

  A data frame with 16 observations on the following 17 variables.

  `treatment`
      a factor with levels `control` `A` `B`

  `gender`
      a factor with levels `F` `M`

  `pre.1`
      pretest, hour 1

  `pre.2`
      pretest, hour 2

  `pre.3`
      pretest, hour 3

  `pre.4`
      pretest, hour 4

  `pre.5`
      pretest, hour 5

  `post.1`
      posttest, hour 1

  `post.2`
      posttest, hour 2

  `post.3`
      posttest, hour 3

  `post.4`
      posttest, hour 4

  `post.5`
      posttest, hour 5

  `fup.1`
      follow-up, hour 1

  `fup.2`
      follow-up, hour 2

  `fup.3`
      follow-up, hour 3

  `fup.4`
      follow-up, hour 4

  `fup.5`
      follow-up, hour 5

  O'Brien, R. G., and Kaiser, M. K. (1985) MANOVA method for analyzing
  repeated measures designs: An extensive primer. *Psychological Bulletin*
  **97**, 316–333, Table 7.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `o_brien_kaiser.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'o_brien_kaiser.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/OBrienKaiser.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='o_brien_kaiser.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
