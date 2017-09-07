from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def karate(path):
  """Load Zachary's Karate Club (Zachary, 1977). It is a social
  network of friendships between 34 members of a karate club at a US
  university from 1970 to 1972. During the study a conflict led the
  club to split into two. Half of the members formed a new club around
  the instructor; members from the other part found a new instructor
  or gave up karate.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `karate.gml`.

  Returns:
    Adjacency matrix as a np.darray `x_train` with 34 rows and 34
    columns.
  """
  import networkx as nx
  path = os.path.expanduser(path)
  filename = 'karate.gml'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://www-personal.umich.edu/~mejn/netdata/karate.zip'
    maybe_download_and_extract(path, url)

  x_train = nx.read_gml(os.path.join(path, filename))
  x_train = nx.to_numpy_matrix(x_train).astype(int)
  return x_train
