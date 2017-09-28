# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def indian_irish(path):
  """Observed genotype frequencies at MN and S loci, for 2 populations

  The `IndianIrish` data frame has 18 rows and 4 columns. The data are
  genotype frequencies for two locations, for Xavante Indian and Irish
  populations respectively

  This data frame contains the following columns:

  Population
      Factor with levels: `Indian` and `Irish`

  locus1
      Factor with levels: `MM`, `MN` and `NN`

  locus2
      Factor with levels: `SS`, `Ss` and `ss`

  Observed
      a numeric vector giving the frequency for each category of the tale

  Mourant et al (1977) and Huttley and Wilson (2000).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `indian_irish.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'indian_irish.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/hwde/IndianIrish.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='indian_irish.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
