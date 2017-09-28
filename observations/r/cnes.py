# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cnes(path):
  """Variables from the 1997 Canadian National Election Study

  These variables are from the mailback questionnaire to the 1997 Canadian
  National Election Study, and are intended to tap attitude towards
  “traditional values.”

  A data frame with 1529 observations on the following 4 variables.

  `MBSA2`
      an ordered factor with levels `StronglyDisagree`, `Disagree`,
      `Agree`, and `StronglyAgree`, in response to the statement, “We
      should be more tolerant of people who choose to live according to
      their own standards, even if they are very different from our own.”

  `MBSA7`
      an ordered factor with levels `StronglyDisagree`, `Disagree`,
      `Agree`, and `StronglyAgree`, in response to the statement,
      “Newer lifestyles are contributing to the breakdown of our society.”

  `MBSA8`
      an ordered factor with levels `StronglyDisagree`, `Disagree`,
      `Agree`, and `StronglyAgree`, in response to the statement, “The
      world is always changing and we should adapt our view of moral
      behaviour to these changes.”

  `MBSA9`
      an ordered factor with levels `StronglyDisagree`, `Disagree`,
      `Agree`, and `StronglyAgree`, in response to the statement,
      “This country would have many fewer problems if there were more
      emphasis on traditional family values.”


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cnes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1529 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cnes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/sem/CNES.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cnes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
