# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def breslow(path):
  """Smoking Deaths Among Doctors

  The `breslow` data frame has 10 rows and 5 columns.

  In 1961 Doll and Hill sent out a questionnaire to all men on the British
  Medical Register enquiring about their smoking habits. Almost 70% of
  such men replied. Death certificates were obtained for medical
  practitioners and causes of death were assigned on the basis of these
  certificates. The `breslow` data set contains the person-years of
  observations and deaths from coronary artery disease accumulated during
  the first ten years of the study.

  This data frame contains the following columns:

  `age`
      The mid-point of the 10 year age-group for the doctors.

  `smoke`
      An indicator of whether the doctors smoked (1) or not (0).

  `n`
      The number of person-years in the category.

  `y`
      The number of deaths attributed to coronary artery disease.

  `ns`
      The number of smoker years in the category (`smoke*n`).

  The data were obtained from

  Breslow, N.E. (1985) Cohort Analysis in Epidemiology. In *A Celebration
  of Statistics* A.C. Atkinson and S.E. Fienberg (editors), 109–143.
  Springer-Verlag.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `breslow.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'breslow.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/breslow.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='breslow.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
