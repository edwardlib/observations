# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cgd(path):
  """Chronic Granulotomous Disease data

  Data are from a placebo controlled trial of gamma interferon in chronic
  granulotomous disease (CGD). Contains the data on time to serious
  infections observed through end of study for each patient.

  id
      subject identification number

  center
      enrolling center

  random
      date of randomization

  treatment
      placebo or gamma interferon

  sex
      sex

  age
      age in years, at study entry

  height
      height in cm at study entry

  weight
      weight in kg at study entry

  inherit
      pattern of inheritance

  steroids
      use of steroids at study entry,1=yes

  propylac
      use of prophylactic antibiotics at study entry

  hos.cat
      a categorization of the centers into 4 groups

  tstart, tstop
      start and end of each time interval

  status
      1=the interval ends with an infection

  enum
      observation number within subject

  Fleming and Harrington, Counting Processes and Survival Analysis,
  appendix D.2.

  See Also
  ~~~~~~~~


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cgd.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 203 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cgd.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/cgd.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cgd.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
