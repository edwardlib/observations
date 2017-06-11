from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def boston_housing(path):
  """Load the Boston Housing data set (Harrison and Rubinfeld, 1978).
    It contains 506 examples of housing values in suburbs of Boston,
    each with 13 continuous attributes and 1 binary attribute.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `housing.data`.

  Returns:
    np.darray `x_train`.
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'housing.data'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
    maybe_download_and_extract(path, url)

  x_train = pd.read_csv(os.path.join(path, filename),
                        header=None, delimiter=r"\s+").as_matrix()
  return x_train
