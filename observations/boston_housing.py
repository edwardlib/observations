from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def boston_housing(path):
  """Load the Boston Housing data set [@harrison1978hedonic].
  It contains 506 examples of housing values in suburbs of Boston,
  each with 13 continuous attributes and 1 binary attribute.

  The data contains the following columns:

  | Feature | Description |
  | --- | --- |
  | CRIM | per capita crime rate by town |
  | ZN | proportion of residential land zoned for lots over 25,000 sq.ft. |
  | INDUS | proportion of non-retail business acres per town. |
  | CHAS | Charles River dummy variable (1 if tract bounds river; 0 otherwise) |
  | NOX | nitric oxides concentration (parts per 10 million) |
  | RM | average number of rooms per dwelling |
  | AGE | proportion of owner-occupied units built prior to 1940 |
  | DIS | weighted distances to five Boston employment centres |
  | RAD | index of accessibility to radial highways |
  | TAX | full-value property-tax rate per $10,000 |
  | PTRATIO | pupil-teacher ratio by town |
  | B | 1000(Bk | 0.63)^2 where Bk is the proportion of blacks by town |
  | LSTAT | % lower status of the population |
  | MEDV | Median value of owner-occupied homes in $1000's |

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `housing.data`.

  Returns:
    Tuple of np.darray `x_train` and dictionary `metadata` of column
    headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'housing.data'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/' \
          'housing/housing.data'
    maybe_download_and_extract(path, url)

  x_train = pd.read_csv(os.path.join(path, filename),
                        header=None, delimiter=r"\s+").as_matrix()
  columns = ['CRIM',
             'ZN',
             'INDUS',
             'CHAS',
             'NOX',
             'RM',
             'AGE',
             'DIS',
             'RAD',
             'TAX',
             'PTRATIO',
             'B',
             'LSTAT',
             'MEDV']
  metadata = {'columns': columns}
  return x_train, metadata
