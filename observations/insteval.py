from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def insteval(path):
  """Load the InstEval data set. It contains 73,421 university lecture
  evaluations by students at ETH Zurich with a total of 2,972
  students, 2,160 professors and lecturers, and several student,
  lecture, and lecturer attributes.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `insteval.csv`.

  Returns:
    Tuple of np.darray `x_train` with 73,421 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = 'InstEval.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/' \
          'lme4/InstEval.csv'
    maybe_download_and_extract(path, url)

  with open(os.path.join(path, filename)) as f:
    iterator = csv.reader(f)
    columns = next(iterator)[1:]
    x_train = []
    x_train = np.array([row[1:] for row in iterator], dtype=np.int)

  metadata = {'columns': columns}
  return x_train, metadata
