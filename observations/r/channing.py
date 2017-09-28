# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def channing(path):
  """Channing House Data

  The `channing` data frame has 462 rows and 5 columns.

  Channing House is a retirement centre in Palo Alto, California. These
  data were collected between the opening of the house in 1964 until July
  1, 1975. In that time 97 men and 365 women passed through the centre.
  For each of these, their age on entry and also on leaving or death was
  recorded. A large number of the observations were censored mainly due to
  the resident being alive on July 1, 1975 when the data was collected.
  Over the time of the study 130 women and 46 men died at Channing House.
  Differences between the survival of the sexes, taking age into account,
  was one of the primary concerns of this study.

  This data frame contains the following columns:

  `sex`
      A factor for the sex of each resident (`"Male"` or `"Female"`).

  `entry`
      The residents age (in months) on entry to the centre

  `exit`
      The age (in months) of the resident on death, leaving the centre or
      July 1, 1975 whichever event occurred first.

  `time`
      The length of time (in months) that the resident spent at Channing
      House. (`time=exit-entry`)

  `cens`
      The indicator of right censoring. 1 indicates that the resident died
      at Channing House, 0 indicates that they left the house prior to
      July 1, 1975 or that they were still alive and living in the centre
      at that date.

  The data were obtained from

  Hyde, J. (1980) Testing survival with incomplete observations.
  *Biostatistics Casebook*. R.G. Miller, B. Efron, B.W. Brown and L.E.
  Moses (editors), 31–46. John Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `channing.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 462 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'channing.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/channing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='channing.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
