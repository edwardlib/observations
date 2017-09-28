# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nitrofen(path):
  """Toxicity of Nitrofen in Aquatic Systems

  The `nitrofen` data frame has 50 rows and 5 columns.

  Nitrofen is a herbicide that was used extensively for the control of
  broad-leaved and grass weeds in cereals and rice. Although it is
  relatively non-toxic to adult mammals, nitrofen is a significant
  tetragen and mutagen. It is also acutely toxic and reproductively toxic
  to cladoceran zooplankton. Nitrofen is no longer in commercial use in
  the U.S., having been the first pesticide to be withdrawn due to
  tetragenic effects.

  The data here come from an experiment to measure the reproductive
  toxicity of nitrofen on a species of zooplankton (*Ceriodaphnia dubia*).
  50 animals were randomized into batches of 10 and each batch was put in
  a solution with a measured concentration of nitrofen. Then the number of
  live offspring in each of the three broods to each animal was recorded.

  This data frame contains the following columns:

  `conc`
      The nitrofen concentration in the solution (mug/litre).

  `brood1`
      The number of live offspring in the first brood.

  `brood2`
      The number of live offspring in the second brood.

  `brood3`
      The number of live offspring in the third brood.

  `total`
      The total number of live offspring in the first three broods.

  The data were obtained from

  Bailer, A.J. and Oris, J.T. (1994) Assessing toxicity of pollutants in
  aquatic systems. In *Case Studies in Biometry*. N. Lange, L. Ryan, L.
  Billard, D. Brillinger, L. Conquest and J. Greenhouse (editors), 25–40.
  John Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nitrofen.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nitrofen.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/nitrofen.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nitrofen.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
