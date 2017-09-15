from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def crabs(path):
  """Load the Crabs data set [@campbell1974multivariate].
  It contains 200 rows and 8 columns, describing 5 morphological
  measurements on 50 crabs each of two colour forms and both sexes, of
  the species Leptograpsus variegatus collected at Fremantle, W.
  Australia.

  The data contains the following columns:

  | Feature | Description |
  | --- | --- |
  | sp | species; 0 for blue, 1 for orange |
  | sex | 0 for male, 1 for female|
  | index | index 1:50 within each of the four groups |
  | FL | frontal lobe size (mm) |
  | RW | rear width (mm) |
  | CL | carapace length (mm) |
  | CW | carapace width (mm) |
  | BD | body depth (mm) |

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `crabs.csv`.

  Returns:
    Tuple of np.darray `x_train` with 200 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = 'crabs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/' \
          'MASS/crabs.csv'
    maybe_download_and_extract(path, url, resume=False)

  species_encoder = {'B': 0, 'O': 1}
  sex_encoder = {'M': 0, 'F': 1}
  with open(os.path.join(path, filename)) as f:
    iterator = csv.reader(f)
    columns = next(iterator)[1:]
    x_train = []
    for row in iterator:
      row = row[1:]
      row[0] = species_encoder[row[0]]
      row[1] = sex_encoder[row[1]]
      x_train.append(row)

  x_train = np.array(x_train, dtype=np.float)
  metadata = {'columns': columns}
  return x_train, metadata
