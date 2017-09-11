from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os

from observations.util import maybe_download_and_extract


def karate(path):
  """Load Zachary's Karate Club [@zachary1977information].
  It is a social network of friendships between 34 members of a karate
  club at a US university from 1970 to 1972. During the study a
  conflict between instructor 'Mr. Hi' and administrator 'Officer' led
  the club to split into two. Half of the members formed a new club
  around 'Mr.  Hi'; other members found a new instructor or quit karate.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `karate.gml`.

  Returns:
    Tuple of adjacency matrix as a np.darray `x_train` with 34 rows
    and 34 columns and np.darray `y_train` of class memberships (0 for
    'Mr.Hi' and 1 for 'Officer').
  """
  import networkx as nx
  path = os.path.expanduser(path)
  filename = 'karate.gml'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://www-personal.umich.edu/~mejn/netdata/karate.zip'
    maybe_download_and_extract(path, url)

  x_train = nx.read_gml(os.path.join(path, filename))
  x_train = nx.to_numpy_matrix(x_train).astype(int)
  labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 21]
  y_train = np.array([0 if i in labels else 1
                      for i in range(x_train.shape[0])], dtype=np.int)
  return x_train, y_train
