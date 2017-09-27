# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def framing(path):
  """Brader, Valentino and Suhay (2008) Framing Experiment Data

  The `framing` data contains 265 rows and 15 columns of data from a
  framing experiment conducted by Brader, Valentino and Suhay (2008).

  A data frame containing the following variables:

  immigr:
      A four-point scale measuring subjects' attitudes toward increased
      immigration. Larger values indicate more negative attitudes.

  english:
      A four-point scale indicating whether subjects favor or oppose a law
      making English the official language of the U.S.

  cong\_mesg:
      Whether subjects requested sending an anti-immigration message to
      Congress on their behalf.

  anti\_info:
      Whether subjects wanted to receive information from anti-immigration
      organizations.

  tone:
      1st treatment; whether the news story is framed positively or
      negatively.

  eth:
      2nd treatment; whether the news story features a Latino or European
      immigrant.

  cond:
      Four level measure recording joint treatment status of tone and eth.

  treat:
      Product of the two treatment variables. In the original study the
      authors only find this cell to be significant.

  emo:
      Measure of subjects' negative feeling during the experiment. A
      numeric scale ranging between 3 and 12 where 3 indicates the most
      negative feeling.

  anx:
      A four-point scale measuring subjects' anxiety about increased
      immigration.

  p\_harm:
      Subjects' perceived harm caused by increased immigration. A numeric
      scale between 2 and 8.

  age:
      Subjects' age.

  educ:
      Subjects' highest educational attainments.

  gender:
      Subjects' gender.

  income:
      Subjects' income, measured as a 19-point scale.

  Brader, T., Valentino, N. and Suhay, E. (2008). What triggers public
  opposition to immigration? Anxiety, group cues, and immigration threat.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `framing.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 265 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'framing.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mediation/framing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='framing.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
