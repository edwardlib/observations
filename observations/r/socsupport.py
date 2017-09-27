# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def socsupport(path):
  """Social Support Data

  Data from a survey on social and other kinds of support.

  This data frame contains the following columns:

  gender
      a factor with levels `female`, `male`

  age
      age, in years, with levels `18-20`, `21-24`, `25-30`,
      `31-40`,\ `40+`

  country
      a factor with levels `australia`, `other`

  marital
      a factor with levels `married`, `other`, `single`

  livewith
      a factor with levels `alone`, `friends`, `other`, `parents`,
      `partner`, `residences`

  employment
      a factor with levels `employed fulltime`, `employed part-time`,
      `govt assistance`, `other`, `parental support`

  firstyr
      a factor with levels `first year`, `other`

  enrolment
      a factor with levels `full-time`, `part-time`, `<NA>`

  emotional
      summary of 5 questions on emotional support availability

  emotionalsat
      summary of 5 questions on emotional support satisfaction

  tangible
      summary of 4 questions on availability of tangible support

  tangiblesat
      summary of 4 questions on satisfaction with tangible support

  affect
      summary of 3 questions on availability of affectionate support
      sources

  affectsat
      summary of 3 questions on satisfaction with affectionate support
      sources

  psi
      summary of 3 questions on availability of positive social
      interaction

  psisat
      summary of 3 questions on satisfaction with positive social
      interaction

  esupport
      summary of 4 questions on extent of emotional support sources

  psupport
      summary of 4 questions on extent of practical support sources

  supsources
      summary of 4 questions on extent of social support sources
      (formerly, socsupport)

  BDI
      Score on the Beck depression index (summary of 21 questions)

  Melissa Manning, Psychology, Australian National University

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `socsupport.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 95 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'socsupport.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/socsupport.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='socsupport.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
