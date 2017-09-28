# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pima_tr(path):
  """Diabetes in Pima Indian Women

  A population of women who were at least 21 years old, of Pima Indian
  heritage and living near Phoenix, Arizona, was tested for diabetes
  according to World Health Organization criteria. The data were collected
  by the US National Institute of Diabetes and Digestive and Kidney
  Diseases. We used the 532 complete records after dropping the (mainly
  missing) data on serum insulin.

  These data frames contains the following columns:

  `npreg`
      number of pregnancies.

  `glu`
      plasma glucose concentration in an oral glucose tolerance test.

  `bp`
      diastolic blood pressure (mm Hg).

  `skin`
      triceps skin fold thickness (mm).

  `bmi`
      body mass index (weight in kg/(height in m)\ *\\^2*).

  `ped`
      diabetes pedigree function.

  `age`
      age in years.

  `type`
      `Yes` or `No`, for diabetic according to WHO criteria.

  Smith, J. W., Everhart, J. E., Dickson, W. C., Knowler, W. C. and
  Johannes, R. S. (1988) Using the ADAP learning algorithm to forecast the
  onset of *diabetes mellitus*. In *Proceedings of the Symposium on
  Computer Applications in Medical Care (Washington, 1988),* ed. R. A.
  Greenes, pp. 261–265. Los Alamitos, CA: IEEE Computer Society Press.

  Ripley, B.D. (1996) *Pattern Recognition and Neural Networks.*

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pima_tr.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 200 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pima_tr.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Pima.tr.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pima_tr.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
