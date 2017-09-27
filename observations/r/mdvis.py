# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mdvis(path):
  """mdvis

  Data from a subset of the German Socio-Economic Panel (SOEP). The subset
  was created by Rabe-Hesketh and Skrondal (2005). Only working women are
  included in these data. Beginning in 1997, German health reform in part
  entailed a 200 co-payment as well as limits in provider reimbursement.
  Patients were surveyed for the one year panel (1996) prior to and the
  one year panel (1998) after reform to assess whether the number of
  physician visits by patients declined - which was the goal of reform
  legislation. The response, or variable to be explained by the model, is
  numvisit, which indicates the number of patient visits to a physician's
  office during a three month period.

  A data frame with 2,227 observations on the following 13 variables.

  `numvisit`
      visits to MD office 3mo prior

  `reform`
      1=interview yr post-reform: 1998;0=pre-reform:1996

  `badh`
      1=bad health; 0 = not bad health

  `age`
      Age(yrs 20-60)

  `educ`
      education(1:7-10;2=10.5-12;3=HSgrad+)

  `educ1`
      educ1= 7-10 years

  `educ2`
      educ2= 10.5-12 years

  `educ3`
      educ3= post secondary or high school

  `agegrp`
      age: 1=20-39; 2=40-49; 3=50-60

  `age1`
      age 20-39

  `age2`
      age 40-49

  `age3`
      age 50-60

  `loginc`
      log(household income in DM)

  German Socio-Economic Panel (SOEP), 1995 pre-reform; 1998 post reform.
  Created by Rabe-Hesketh and Skrondal (2005).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mdvis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2227 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mdvis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/mdvis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mdvis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
