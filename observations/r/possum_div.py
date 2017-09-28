# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def possum_div(path):
  """Possum Diversity Data

  Possum diversity data: As issued from a study of the diversity of possum
  (arboreal marsupials) in the Montane ash forest (Australia), this
  dataset was collected in view of the management of hardwood forest to
  take conservation and recreation values, as well as wood production,
  into account.

  The study is fully described in the two references. The number of
  different species of arboreal marsupials (possum) was observed on 151
  different 3ha sites with uniform vegetation. For each site the nine
  variable measures (see below) were recorded. The problem is to model the
  relationship between `diversity` and these other variables.

  Two different representations of the same data are available:

  `possumDiv` is a data frame of 151 observations of 9 variables, where
  the last two are factors, `eucalyptus` with 3 levels and `aspect`
  with 4 levels.

  `possum.mat` is a numeric (integer) matrix of 151 rows (observations)
  and 14 columns (variables) where the last seven ones are 0-1 dummy
  variables, three (`E.*`) are coding for the kind of `eucalyptus` and
  the last four are 0-1 coding for the `aspect` factor.

  The variables have the following meaning:

  Diversity
      main variable of interest is the number of different species of
      arboreal marsupial (possum) observed, with values in 0:5.

  Shrubs
      the number of shrubs.

  Stumps
      the number of cut stumps from past logging operations.

  Stags
      the number of stags (hollow-bearing trees).

  Bark
      bark index (integer) vector reflecting the quantity of decorticating
      bark.

  Habitat
      an integer score indicating the suitability of nesting and foraging
      habitat for Leadbeater's possum.

  BAcacia
      a numeric vector giving the basal area of acacia species.

  eucalyptus
      a 3-level `factor` specifying the species of eucalypt with the
      greatest stand basal area. This has the same information as the
      following three variables

  E.regnans
      0-1 indicator for Eucalyptus regnans

  E.delegatensis
      0-1 indicator for Eucalyptus deleg.

  E.nitens
      0-1 indicator for Eucalyptus nitens

  aspect
      a 4-level `factor` specifying the aspect of the site. It is the
      same information as the following four variables.

  NW-NE
      0-1 indicator

  NW-SE
      0-1 indicator

  SE-SW
      0-1 indicator

  SW-NW
      0-1 indicator

  Eva Cantoni (2004) Analysis of Robust Quasi-deviances for Generalized
  Linear Models. *Journal of Statistical Software* **10**, 04,
  http://www.jstatsoft.org/v10/i04

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `possum_div.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 151 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'possum_div.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/possumDiv.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='possum_div.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
