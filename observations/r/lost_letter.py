# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lost_letter(path):
  """LostLetter

  Which "lost" letters will be returned by the public?

  A dataset with 140 observations on the following 8 variables.

  `Location`

  Where letter was "lost": `DesMoines`, `GrinnellCampus`, or
  `GrinnellTown`

  `Address`

  Address on teh letter: `Confederacy` or `Peaceworks`

  `Returned`

  `1`\ =letter was returned or `0`\ =letter was not returned

  `DesMoines`

  Indicator for letters left in Des Moines

  `GrinnellTown`

  Indicator for letters left in the town of Grinnell

  `GrinellCampus`

  Indicator for letters left on the Grinnell campus

  `Peaceworks`

  Indicator for letters addressed to Iowa Peaceworks

  `Confederacy`

  Indicator for letters addressed to Friends of the Confederacy


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lost_letter.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 140 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lost_letter.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/LostLetter.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lost_letter.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
