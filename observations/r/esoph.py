# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def esoph(path):
  """Smoking, Alcohol and (O)esophageal Cancer

  Data from a case-control study of (o)esophageal cancer in
  Ille-et-Vilaine, France.

  A data frame with records for 88 age/alcohol/tobacco combinations.

+------------+--------------------+--------------------+--------------------+
| [,1]       | "agegp"            | Age group          | 1 25--34 years     |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 2 35--44           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 3 45--54           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 4 55--64           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 5 65--74           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 6 75+              |
+------------+--------------------+--------------------+--------------------+
| [,2]       | "alcgp"            | Alcohol            | 1 0--39 gm/day     |
|            |                    | consumption        |                    |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 2 40--79           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 3 80--119          |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 4 120+             |
+------------+--------------------+--------------------+--------------------+
| [,3]       | "tobgp"            | Tobacco            | 1 0-- 9 gm/day     |
|            |                    | consumption        |                    |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 2 10--19           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 3 20--29           |
+------------+--------------------+--------------------+--------------------+
|            |                    |                    | 4 30+              |
+------------+--------------------+--------------------+--------------------+
| [,4]       | "ncases"           | Number of cases    |                    |
+------------+--------------------+--------------------+--------------------+
| [,5]       | "ncontrols"        | Number of controls |                    |
+------------+--------------------+--------------------+--------------------+

  Author(s)
  ~~~~~~~~~

  Thomas Lumley

  Breslow, N. E. and Day, N. E. (1980) *Statistical Methods in Cancer
  Research. Volume 1: The Analysis of Case-Control Studies.* IARC Lyon /
  Oxford University Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `esoph.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 88 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'esoph.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/esoph.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='esoph.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
