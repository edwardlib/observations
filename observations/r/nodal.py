# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nodal(path):
  """Nodal Involvement in Prostate Cancer

  The `nodal` data frame has 53 rows and 7 columns.

  The treatment strategy for a patient diagnosed with cancer of the
  prostate depend highly on whether the cancer has spread to the
  surrounding lymph nodes. It is common to operate on the patient to get
  samples from the nodes which can then be analysed under a microscope but
  clearly it would be preferable if an accurate assessment of nodal
  involvement could be made without surgery.

  For a sample of 53 prostate cancer patients, a number of possible
  predictor variables were measured before surgery. The patients then had
  surgery to determine nodal involvement. It was required to see if nodal
  involvement could be accurately predicted from the predictor variables
  and which ones were most important.

  This data frame contains the following columns:

  `m`
      A column of ones.

  `r`
      An indicator of nodal involvement.

  `aged`
      The patients age dichotomized into less than 60 (`0`) and 60 or
      over `1`.

  `stage`
      A measurement of the size and position of the tumour observed by
      palpitation with the fingers via the rectum. A value of `1`
      indicates a more serious case of the cancer.

  `grade`
      Another indicator of the seriousness of the cancer, this one is
      determined by a pathology reading of a biopsy taken by needle before
      surgery. A value of `1` indicates a more serious case of the
      cancer.

  `xray`
      A third measure of the seriousness of the cancer taken from an X-ray
      reading. A value of `1` indicates a more serious case of the
      cancer.

  `acid`
      The level of acid phosphatase in the blood serum.

  The data were obtained from

  Brown, B.W. (1980) Prediction analysis for binary data. In
  *Biostatistics Casebook*. R.G. Miller, B. Efron, B.W. Brown and L.E.
  Moses (editors), 3–18. John Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nodal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 53 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nodal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/nodal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nodal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
