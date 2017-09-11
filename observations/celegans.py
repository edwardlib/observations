from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os

from observations.util import maybe_download_and_extract


def celegans(path):
  """Load the neural network of the worm C. Elegans [@watts1998collective].
  The neural network consists of around 300 neurons. Each connection
  between neurons is associated with a weight (positive integer)
  capturing the strength of the connection.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `celegansneural.gml`.

  Returns:
    Adjacency matrix as a np.darray `x_train` with 297 rows and 297
    columns.
  """
  import networkx as nx
  path = os.path.expanduser(path)
  filename = 'celegansneural.gml'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://www-personal.umich.edu/~mejn/netdata/celegansneural.zip'
    maybe_download_and_extract(path, url)

  graph = nx.read_gml(os.path.join(path, filename))
  x_train = np.zeros([graph.number_of_nodes(), graph.number_of_nodes()],
                     dtype=np.int)
  for i, j in graph.edges():
    x_train[i, j] = int(graph[i][j][0]['value'])
  return x_train
