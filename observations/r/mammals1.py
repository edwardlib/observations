from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mammals1(path):
  """Garland(1983) Data on Running Speed of Mammals

  Observations on the maximal running speed of mammal species and their
  body mass.

  A data frame with 107 observations on the following 4 variables.

  weight
      Body mass in Kg for "typical adult sizes"

  speed
      Maximal running speed (fastest sprint velocity on record)

  hoppers
      logical variable indicating animals that ambulate by hopping, e.g.
      kangaroos

  specials
      logical variable indicating special animals with "lifestyles in
      which speed does not figure as an important factor": Hippopotamus,
      raccoon (Procyon), badger (Meles), coati (Nasua), skunk (Mephitis),
      man (Homo), porcupine (Erithizon), oppossum (didelphis), and sloth
      (Bradypus)

  Garland, T. (1983) The relation between maximal running speed and body
  mass in terrestrial mammals, *J. Zoology*, 199, 1557-1570.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mammals1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 107 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mammals1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/quantreg/Mammals.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mammals1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
