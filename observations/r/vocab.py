# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vocab(path):
  """Vocabulary and Education

  The `Vocab` data frame has 21,638 rows and 5 columns. The observations
  are respondents to U.S. General Social Surveys, 1972-2004.

  This data frame contains the following columns:

  year
      Year of the survey.

  sex
      Sex of the respondent, `Female` or `Male`.

  education
      Education, in years.

  vocabulary
      Vocabulary test score: number correct on a 10-word test.

  National Opinion Research Center *General Social Survey.* GSS Cumulative
  Datafile 1972-2004, downloaded from http://sda.berkeley.edu/archive.htm.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vocab.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21638 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vocab.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Vocab.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vocab.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
