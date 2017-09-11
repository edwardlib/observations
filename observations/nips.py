from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def nips(path):
  """Load the NIPS conference papers 1987-2015 data set [@perrone2016poisson].
  It is in the form of a 11,463 x 5,812 matrix of word counts,
  containing 11,463 words and 5,811 NIPS conference papers (the first
  column contains the list of words). Each column contains the number
  of times each word appears in the corresponding document.  The names
  of the columns give information about each document and its
  timestamp in the following format: `year_paperID`.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `NIPS_1987-2015.csv`.

  Returns:
    Tuple of np.darray `x_train` and dictionary `metadata` of column
    headers (documents) and row headers (words).
  """
  path = os.path.expanduser(path)
  filename = 'NIPS_1987-2015.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/' \
          '00371/NIPS_1987-2015.csv'
    maybe_download_and_extract(path, url)

  with open(os.path.join(path, filename)) as f:
    iterator = csv.reader(f)
    documents = next(iterator)[1:]
    words = []
    x_train = []
    for row in iterator:
      words.append(row[0])
      x_train.append(row[1:])

  x_train = np.array(x_train, dtype=np.int)
  metadata = {'columns': documents, 'rows': words}
  return x_train, metadata
