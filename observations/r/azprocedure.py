# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def azprocedure(path):
  """azprocedure

  Data come from the 1991 Arizona cardiovascular patient files. A subset
  of the fields was selected to model the differential length of stay for
  patients entering the hospital to receive one of two standard
  cardiovascular procedures: CABG and PTCA. CABG is the standard acronym
  for Coronary Artery Bypass Graft, where the flow of blood in a diseased
  or blocked coronary artery or vein has been grafted to bypass the
  diseased sections. PTCA, or Percutaneous Transluminal Coronary
  Angioplasty, is a method of placing a balloon in a blocked coronary
  artery to open it to blood flow. It is a much less severe method of
  treatment for those having coronary blockage, with a corresponding
  reduction in risk.

  A data frame with 3589 observations on the following 6 variables.

  `los`
      length of hospital stay

  `procedure`
      1=CABG;0=PTCA

  `sex`
      1=Male; 0=female

  `admit`
      1=Urgent/Emerg; 0=elective (type of admission)

  `age75`
      1= Age>75; 0=Age<=75

  `hospital`
      encrypted facility code (string)

  1991 Arizona Medpar data, cardiovascular patient files, National Health
  Economics & Research Co.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `azprocedure.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3589 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'azprocedure.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/azprocedure.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='azprocedure.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
