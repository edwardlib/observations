# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def greene(path):
  """Refugee Appeals

  The `Greene` data frame has 384 rows and 7 columns. These are cases
  filed in 1990, in which refugee claimants rejected by the Canadian
  Immigration and Refugee Board asked the Federal Court of Appeal for
  leave to appeal the negative ruling of the Board.

  This data frame contains the following columns:

  judge
      Name of judge hearing case. A factor with levels: `Desjardins`,
      `Heald`, `Hugessen`, `Iacobucci`, `MacGuigan`, `Mahoney`,
      `Marceau`, `Pratte`, `Stone`, `Urie`.

  nation
      Nation of origin of claimant. A factor with levels: `Argentina`,
      `Bulgaria`, `China`, `Czechoslovakia`, `El.Salvador`,
      `Fiji`, `Ghana`, `Guatemala`, `India`, `Iran`,
      `Lebanon`, `Nicaragua`, `Nigeria`, `Pakistan`, `Poland`,
      `Somalia`, `Sri.Lanka`.

  rater
      Judgment of independent rater. A factor with levels: `no`, case
      has no merit; `yes`, case has some merit (leave to appeal should
      be granted).

  decision
      Judge's decision. A factor with levels: `no`, leave to appeal not
      granted; `yes`, leave to appeal granted.

  language
      Language of case. A factor with levels: `English`, `French`.

  location
      Location of original refugee claim. A factor with levels:
      `Montreal`, `other`, `Toronto`.

  success
      Logit of success rate, for all cases from the applicant's nation.

  Personal communication from Ian Greene, Department of Political Science,
  York University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `greene.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 384 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'greene.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Greene.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='greene.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
