# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cuckoohosts(path):
  """Comparison of cuckoo eggs with host eggs

  These data compare mean length, mean breadth, and egg color, between
  cuckoos and their hosts.

  A data frame with 10 observations on the following 12 variables.

  clength
      mean length of cuckoo eggs in given host's nest

  cl.sd
      standard deviation of cuckoo egg lengths

  cbreadth
      mean breadth of cuckoo eggs in given host's nest

  cb.sd
      standard deviation of cuckoo egg breadths

  cnum
      number of cuckoo eggs

  hlength
      length of host eggs

  hl.sd
      standard deviation of host egg lengths

  hbreadth
      breadth of host eggs

  hb.sd
      standard deviation of host egg breadths

  hnum
      number of host eggs

  match
      number of eggs where color matched

  nomatch
      number where color did not match

  Latter, O.H., 1902. The egg of *cuculus canorus*. an inquiry into the
  dimensions of the cuckoo's egg and the relation of the variations to the
  size of the eggs of the foster-parent, with notes on coloration, &c.
  *Biometrika*, 1:164–176.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cuckoohosts.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cuckoohosts.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/cuckoohosts.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cuckoohosts.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
