# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pyx(path):
  """Trial of the Pyx

  Stigler (1997, 1999) recounts the history of one of the oldest
  continuous schemes of sampling inspection carried out by the Royal Mint
  in London for about eight centuries. The Trial of the Pyx was the final,
  ceremonial stage in a process designed to ensure that the weight and
  quality of gold and silver coins from the mint met the standards for
  coinage.

  At regular intervals, coins would be taken from production and deposited
  into a box called the Pyx. When a Trial of the Pyx was called, the
  contents of the Pyx would be counted, weighed and assayed for content,
  and the results would be compared with the standard set for the Royal
  Mint.

  The data frame `Pyx` gives the results for the year 1848 (Great
  Britain, 1848) in which 10,000 gold sovereigns were assayed. The coins
  in each bag were classified according to the deviation from the standard
  content of gold for each coin, called the Remedy, R = 123 \* (12/5760) =
  .25625, in grains, for a single sovereign.

  A frequency data frame with 72 observations on the following 4 variables
  giving the distribution of 10,000 soverigns, classified according to the
  `Bags` in which they were collected and the `Deviation` from the
  standard weight.

  `Bags`
      an ordered factor with levels `1 and 2` < `3` < `4` < `5` <
      `6` < `7` < `8` < `9` < `10`

  `Group`
      an ordered factor with levels `below std` < `near std` <
      `above std`

  `Deviation`
      an ordered factor with levels `Below -R` < `(-R to -.2)` <
      `(-.2 to -.l)` < `(-.1 to 0)` < `(0 to .l)` < `(.1 to .2)` <
      `(.2 to R)` < `Above R`

  `count`
      number of soverigns

  Stigler, S. M. (1999). *Statistics on the Table*. Cambridge, MA: Harvard
  University Press, table 21.1.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pyx.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pyx.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Pyx.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pyx.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
