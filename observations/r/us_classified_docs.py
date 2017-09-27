# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_classified_docs(path):
  """Official Secrecy of the United States Government

  Data on classification activity of the United States government.

  Fitzpatrick (2013) notes that the dramatic jump in derivative
  classification activity (`DerivClassActivity`) that occurred in 2009
  coincided with "New guidance issued to include electronic environment".
  Apart from the jump in 2009, the `DerivClassActivity` tended to
  increase by roughly 12 percent per year (with a standard deviation of
  the increase in the natural logarithm of `DerivClassActivity` of
  0.18).

  A dataframe containing :

  year
      the calendar year

  OCAuthority
      Number of people in the government designated as Original
      Classification Authorities for the indicated `year`.

  OCActivity
      Original classification activity for the indicated year: These are
      the number of documents created with an original classification,
      i.e., so designated by an official Original Classification
      Authority.

  TenYearDeclass
      Percent of `OCActivity` covered by the 10 year declassification
      rules.

  DerivClassActivity
      Derivative classification activity for the indicated year: These are
      the number of documents created that claim another document as the
      authority for classification.

  Fitzpatrick, John P. (2013) *Annual Report to the President for 2012*,
  United States Information Security Oversight Office, National Archives
  and Record Administration, June 20, 2013
  (https://www.archives.gov/isoo/reports)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_classified_docs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 29 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_classified_docs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/USclassifiedDocuments.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_classified_docs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
