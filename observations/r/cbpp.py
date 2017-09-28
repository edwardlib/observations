# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cbpp(path):
  """Contagious bovine pleuropneumonia

  Contagious bovine pleuropneumonia (CBPP) is a major disease of cattle in
  Africa, caused by a mycoplasma. This dataset describes the serological
  incidence of CBPP in zebu cattle during a follow-up survey implemented
  in 15 commercial herds located in the Boji district of Ethiopia. The
  goal of the survey was to study the within-herd spread of CBPP in newly
  infected herds. Blood samples were quarterly collected from all animals
  of these herds to determine their CBPP status. These data were used to
  compute the serological incidence of CBPP (new cases occurring during a
  given time period). Some data are missing (lost to follow-up).

  A data frame with 56 observations on the following 4 variables.

  `herd`
      A factor identifying the herd (1 to 15).

  `incidence`
      The number of new serological cases for a given herd and time
      period.

  `size`
      A numeric vector describing herd size at the beginning of a given
      time period.

  `period`
      A factor with levels `1` to `4`.

  Lesnoff, M., Laval, G., Bonnet, P., Abdicho, S., Workalemahu, A., Kifle,
  D., Peyraud, A., Lancelot, R., Thiaucourt, F. (2004) Within-herd spread
  of contagious bovine pleuropneumonia in Ethiopian highlands. *Preventive
  Veterinary Medicine* **64**, 27–40.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cbpp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cbpp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/cbpp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cbpp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
