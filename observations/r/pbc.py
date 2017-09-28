# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pbc(path):
  """Mayo Clinic Primary Biliary Cirrhosis Data

  D This data is from the Mayo Clinic trial in primary biliary cirrhosis
  (PBC) of the liver conducted between 1974 and 1984. A total of 424 PBC
  patients, referred to Mayo Clinic during that ten-year interval, met
  eligibility criteria for the randomized placebo controlled trial of the
  drug D-penicillamine. The first 312 cases in the data set participated
  in the randomized trial and contain largely complete data. The
  additional 112 cases did not participate in the clinical trial, but
  consented to have basic measurements recorded and to be followed for
  survival. Six of those cases were lost to follow-up shortly after
  diagnosis, so the data here are on an additional 106 cases as well as
  the 312 randomized participants.

  A nearly identical data set found in appendix D of Fleming and
  Harrington; this version has fewer missing values.

  age:

  in years

  albumin:

  serum albumin (g/dl)

  alk.phos:

  alkaline phosphotase (U/liter)

  ascites:

  presence of ascites

  ast:

  aspartate aminotransferase, once called SGOT (U/ml)

  bili:

  serum bilirunbin (mg/dl)

  chol:

  serum cholesterol (mg/dl)

  copper:

  urine copper (ug/day)

  edema:

  0 no edema, 0.5 untreated or successfully treated

  1 edema despite diuretic therapy

  hepato:

  presence of hepatomegaly or enlarged liver

  id:

  case number

  platelet:

  platelet count

  protime:

  standardised blood clotting time

  sex:

  m/f

  spiders:

  blood vessel malformations in the skin

  stage:

  histologic stage of disease (needs biopsy)

  status:

  status at endpoint, 0/1/2 for censored, transplant, dead

  time:

  number of days between registration and the earlier of death,

  transplantion, or study analysis in July, 1986

  trt:

  1/2/NA for D-penicillmain, placebo, not randomised

  trig:

  triglycerides (mg/dl)

  T Therneau and P Grambsch (2000), *Modeling Survival Data: Extending the

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pbc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 418 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pbc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/pbc.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pbc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
