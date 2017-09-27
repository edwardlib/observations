# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def colon(path):
  """Chemotherapy for Stage B/C colon cancer

  These are data from one of the first successful trials of adjuvant
  chemotherapy for colon cancer. Levamisole is a low-toxicity compound
  previously used to treat worm infestations in animals; 5-FU is a
  moderately toxic (as these things go) chemotherapy agent. There are two
  records per person, one for recurrence and one for death

  id:

  id

  study:

  1 for all patients

  rx:

  Treatment - Obs(ervation), Lev(amisole), Lev(amisole)+5-FU

  sex:

  1=male

  age:

  in years

  obstruct:

  obstruction of colon by tumour

  perfor:

  perforation of colon

  adhere:

  adherence to nearby organs

  nodes:

  number of lymph nodes with detectable cancer

  time:

  days until event or censoring

  status:

  censoring status

  differ:

  differentiation of tumour (1=well, 2=moderate, 3=poor)

  extent:

  Extent of local spread (1=submucosa, 2=muscle, 3=serosa, 4=contiguous
  structures)

  surg:

  time from surgery to registration (0=short, 1=long)

  node4:

  more than 4 positive lymph nodes

  etype:

  event type: 1=recurrence,2=death

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `colon.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1858 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'colon.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/colon.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='colon.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
