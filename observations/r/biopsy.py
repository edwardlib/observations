# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def biopsy(path):
  """Biopsy Data on Breast Cancer Patients

  This breast cancer database was obtained from the University of
  Wisconsin Hospitals, Madison from Dr. William H. Wolberg. He assessed
  biopsies of breast tumours for 699 patients up to 15 July 1992; each of
  nine attributes has been scored on a scale of 1 to 10, and the outcome
  is also known. There are 699 rows and 11 columns.

  This data frame contains the following columns:

  `ID`
      sample code number (not unique).

  `V1`
      clump thickness.

  `V2`
      uniformity of cell size.

  `V3`
      uniformity of cell shape.

  `V4`
      marginal adhesion.

  `V5`
      single epithelial cell size.

  `V6`
      bare nuclei (16 values are missing).

  `V7`
      bland chromatin.

  `V8`
      normal nucleoli.

  `V9`
      mitoses.

  `class`
      `"benign"` or `"malignant"`.

  P. M. Murphy and D. W. Aha (1992). UCI Repository of machine learning
  databases. [Machine-readable data repository]. Irvine, CA: University of
  California, Department of Information and Computer Science.

  O. L. Mangasarian and W. H. Wolberg (1990) Cancer diagnosis via linear
  programming. *SIAM News* **23**, pp 1 & 18.

  William H. Wolberg and O.L. Mangasarian (1990) Multisurface method of
  pattern separation for medical diagnosis applied to breast cytology.
  *Proceedings of the National Academy of Sciences, U.S.A.* **87**, pp.
  9193–9196.

  O. L. Mangasarian, R. Setiono and W.H. Wolberg (1990) Pattern
  recognition via linear programming: Theory and application to medical
  diagnosis. In *Large-scale Numerical Optimization* eds Thomas F. Coleman
  and Yuying Li, SIAM Publications, Philadelphia, pp 22–30.

  K. P. Bennett and O. L. Mangasarian (1992) Robust linear programming
  discrimination of two linearly inseparable sets. *Optimization Methods
  and Software* **1**, pp. 23–34 (Gordon & Breach Science Publishers).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `biopsy.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 699 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'biopsy.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/biopsy.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='biopsy.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
