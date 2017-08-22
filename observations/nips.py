from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def nips(path, year=None):
  """Load the NIPS conference papers 1987-2015 data set (Perrone et
  al., 2016). It is in the form of a 11,463 x 5,812 matrix of word
  counts, containing 11,463 words and 5,811 NIPS conference papers
  (the first column contains the list of words). Each column contains
  the number of times each word appears in the corresponding document.
  The names of the columns give information about each document and
  its timestamp in the following format: `year_paperID`.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `NIPS_1987-2015.csv`.
    year: int or list, optional.
      Year or list of years to subset data. We subset to documents in
      `year` and words appearing at least once in the document subset.

  Returns:
    # TODO c.f., other returns for returning metadata
    Tuple of np.darray `x_train`, column headers `documents`, and row
    headers `words`.
  """
  if isinstance(year, int):
    year = [year]
  path = os.path.expanduser(path)
  filename = 'NIPS_1987-2015.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00371/NIPS_1987-2015.csv'
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
  if year is not None:
    doc_idx = [i for i, document in enumerate(documents)
               if document.startswith(tuple(year))]
    documents = [documents[doc] for doc in doc_idx]
    x_train = x_train[:, doc_idx]
    word_idx = np.sum(x_train, 1) != 0
    words = [words[word] for word in word_idx]
    x_train = x_train[word_idx, :]

  return x_train, documents, words
