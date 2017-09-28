# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def doctor_contacts(path):
  """Contacts With Medical Doctor

  a cross-section from 1977–1978

  *number of observations* : 20186

  A time serie containing :

  mdu
      number of outpatient visits to a medical doctor

  lc
      log(coinsrate+1) where coinsurance rate is 0 to 100

  idp
      individual deductible plan ?

  lpi
      log(annual participation incentive payment) or 0 if no payment

  fmde
      log(max(medical deductible expenditure)) if IDP=1 and MDE>1 or 0
      otherw

  physlim
      physical limitation ?

  ndisease
      number of chronic diseases

  health
      self–rate health (excellent,good,fair,poor)

  linc
      log of annual family income (in \\$)

  lfam
      log of family size

  educdec
      years of schooling of household head

  age
      exact age

  sex
      sex (male,female)

  child
      age less than 18 ?

  black
      is household head black ?

  Deb, P. and P.K. Trivedi (2002) “The Structure of Demand for Medical
  Care: Latent Class versus Two-Part Models”, *Journal of Health
  Economics*, **21**, 601–625.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `doctor_contacts.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20186 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'doctor_contacts.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/DoctorContacts.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='doctor_contacts.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
