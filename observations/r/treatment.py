# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def treatment(path):
  """Evaluating Treatment Effect of Training on Earnings

  a cross-section from 1974

  *number of observations* : 2675

  *country* : United States

  A dataframe containing :

  treat
      treated ?

  age
      age

  educ
      education in years

  ethn
      a factor with levels ("other","black","hispanic")

  married
      married ?

  re74
      real annual earnings in 1974 (pre-treatment)

  re75
      real annual earnings in 1975 (pre-treatment)

  re78
      real annual earnings in 1978 (post-treatment)

  u74
      unemployed in 1974 ?

  u75
      unemployed in 1975 ?

  Lalonde, R. (1986) “Evaluating the Econometric Evaluations of Training
  Programs with Experimental Data”, *American Economic Review*, 604–620.

  Dehejia, R.H. and S. Wahba (1999) “Causal Effects in Nonexperimental
  Studies: reevaluating the Evaluation of Training Programs”, *Jasa*,
  1053–1062.

  Dehejia, R.H. and S. Wahba (2002) “Propensity-score Matching Methods for
  Nonexperimental Causal Studies”, *Restat*, 151–161.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `treatment.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2675 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'treatment.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Treatment.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='treatment.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
