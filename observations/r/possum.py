# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def possum(path):
  """Possum Measurements

  The `possum` data frame consists of nine morphometric measurements on
  each of 104 mountain brushtail possums, trapped at seven sites from
  Southern Victoria to central Queensland.

  This data frame contains the following columns:

  case
      observation number

  site
      one of seven locations where possums were trapped

  Pop
      a factor which classifies the sites as `Vic` Victoria, `other`
      New South Wales or Queensland

  sex
      a factor with levels `f` female, `m` male

  age
      age

  hdlngth
      head length

  skullw
      skull width

  totlngth
      total length

  taill
      tail length

  footlgth
      foot length

  earconch
      ear conch length

  eye
      distance from medial canthus to lateral canthus of right eye

  chest
      chest girth (in cm)

  belly
      belly girth (in cm)

  Lindenmayer, D. B., Viggers, K. L., Cunningham, R. B., and Donnelly, C.
  F. 1995. Morphological variation among columns of the mountain brushtail
  possum, Trichosurus caninus Ogilby (Phalangeridae: Marsupiala).
  Australian Journal of Zoology 43: 449-458.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `possum.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 104 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'possum.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/possum.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='possum.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
