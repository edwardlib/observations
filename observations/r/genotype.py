# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def genotype(path):
  """Rat Genotype Data

  Data from a foster feeding experiment with rat mothers and litters of
  four different genotypes: `A`, `B`, `I` and `J`. Rat litters
  were separated from their natural mothers at birth and given to foster
  mothers to rear.

  The data frame has the following components:

  `Litter`
      genotype of the litter.

  `Mother`
      genotype of the foster mother.

  `Wt`
      Litter average weight gain of the litter, in grams at age 28 days.
      (The source states that the within-litter variability is
      negligible.)

  Scheffe, H. (1959) *The Analysis of Variance* Wiley p. 140.

  Bailey, D. W. (1953) *The Inheritance of Maternal Influences on the
  Growth of the Rat.* Unpublished Ph.D. thesis, University of California.
  Table B of the Appendix.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `genotype.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 61 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'genotype.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/genotype.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='genotype.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
