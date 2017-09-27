# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def iris(path):
  """Edgar Anderson's Iris Data

  This famous (Fisher's or Anderson's) iris data set gives the
  measurements in centimeters of the variables sepal length and width and
  petal length and width, respectively, for 50 flowers from each of 3
  species of iris. The species are *Iris setosa*, *versicolor*, and
  *virginica*.

  `iris` is a data frame with 150 cases (rows) and 5 variables (columns)
  named `Sepal.Length`, `Sepal.Width`, `Petal.Length`,
  `Petal.Width`, and `Species`.

  `iris3` gives the same data arranged as a 3-dimensional array of size
  50 by 4 by 3, as represented by S-PLUS. The first dimension gives the
  case number within the species subsample, the second the measurements
  with names `Sepal L.`, `Sepal W.`, `Petal L.`, and `Petal W.`,
  and the third the species.

  Fisher, R. A. (1936) The use of multiple measurements in taxonomic
  problems. *Annals of Eugenics*, **7**, Part II, 179–188.

  The data were collected by Anderson, Edgar (1935). The irises of the
  Gaspe Peninsula, *Bulletin of the American Iris Society*, **59**, 2–5.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `iris.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 150 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'iris.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/iris.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='iris.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
