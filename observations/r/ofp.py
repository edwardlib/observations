# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ofp(path):
  """Visits to Physician Office

  a cross-section

  *number of observations* : 4406

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  ofp
      number of physician office visits

  ofnp
      number of nonphysician office visits

  opp
      number of physician outpatient visits

  opnp
      number of nonphysician outpatient visits

  emr
      number of emergency room visits

  hosp
      number of hospitalizations

  numchron
      number of chronic conditions

  adldiff
      the person has a condition that limits activities of daily living ?

  age
      age in years (divided by 10)

  black
      is the person african–american ?

  sex
      is the person male ?

  maried
      is the person maried ?

  school
      number of years of education

  faminc
      family income in 10000\\$

  employed
      is the person employed ?

  privins
      is the person covered by private health insurance ?

  medicaid
      is the person covered by medicaid ?

  region
      the region (noreast, midwest,west)

  hlth
      self-perceived health (excellent, poor, other)

  Deb, P. and P.K. Trivedi (1997) “Demand for Medical Care by the Elderly:
  A Finite Mixture Approach”, *Journal of Applied Econometrics*, **12**,
  313-326..

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ofp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4406 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ofp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/OFP.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ofp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
