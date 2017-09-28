# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def drinks_wages(path):
  """Elderton and Pearson's (1910) data on drinking and wages

  In 1910, Karl Pearson weighed in on the debate, fostered by the
  temperance movement, on the evils done by alcohol not only to drinkers,
  but to their families. The report "A first study of the influence of
  parental alcholism on the physique and ability of their offspring" was
  an ambitious attempt to the new methods of statistics to bear on an
  important question of social policy, to see if the hypothesis that
  children were damaged by parental alcoholism would stand up to
  statistical scrutiny.

  Working with his assistant, Ethel M. Elderton, Pearson collected
  voluminous data in Edinburgh and Manchester on many aspects of health,
  stature, intelligence, etc. of children classified according to the
  drinking habits of their parents. His conclusions where almost
  invariably negative: the tendency of parents to drink appeared unrelated
  to any thing he had measured.

  The firestorm that this report set off is well described by Stigler
  (1999), Chapter 1. The data set `DrinksWages` is just one of Pearsons
  many tables, that he published in a letter to *The Times*, August 10,
  1910.

  A data frame with 70 observations on the following 6 variables, giving
  the number of non-drinkers (`sober`) and drinkers (`drinks`) in
  various occupational categories (`trade`).

  `class`
      wage class: a factor with levels `A` `B` `C`

  `trade`
      a factor with levels `baker` `barman` `billposter` ...
      `wellsinker` `wireworker`

  `sober`
      the number of non-drinkers, a numeric vector

  `drinks`
      the number of drinkers, a numeric vector

  `wage`
      weekly wage (in shillings), a numeric vector

  `n`
      total number, a numeric vector

  Pearson, K. (1910). *The Times*, August 10, 1910.

  Stigler, S. M. (1999). *Statistics on the Table: The History of
  Statistical Concepts and Methods*. Harvard University Press, Table 1.1

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `drinks_wages.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 70 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'drinks_wages.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/DrinksWages.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='drinks_wages.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
