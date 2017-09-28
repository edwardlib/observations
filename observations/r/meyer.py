# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def meyer(path):
  """A pedigree data on 282 animals deriving from two generations

  A data frame attributed to Meyer (1989).

  “The pedigrees for each of these 282 animals derive from an additional
  24 base population (Generation 0) animals that do not have records of
  their own but, nevertheless, are of interest with respect to the
  inference on their own additive genetic values. Furthermore, it is
  presumed that these original 24 base animals are not related to each
  other. Therefore, the row dimension of u is 306 (282+24).” (Templeman
  \\& Rosa 2004)

  A data frame containing 306 records

  Meyer K (1989). Restricted maximum likelihood to estimate variance
  components for animal models with several random effects using a
  derivative-free algorithm. Genetics, Selection, Evolution 21:317-340.

  Tempelman RJ, Rosa GJM. Empirical Bayes Approaches to Mixed Model
  Inference in Quantitative Genetics. in Saxton AM (Ed). Genetic Analysis
  of Complex Traits Using SAS, chapter 7. SAS Institute Inc., Cary, NC,
  USA, 2004

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `meyer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 306 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'meyer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gap/meyer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='meyer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
