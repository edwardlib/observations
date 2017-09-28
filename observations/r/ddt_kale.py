# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ddt_kale(path):
  """DDT in Kale

  A numeric vector of 15 measurements by different laboratories of the
  pesticide DDT in kale, in ppm (parts per million) using the multiple
  pesticide residue measurement.

  C. E. Finsterwalder (1976) Collaborative study of an extension of the
  Mills *et al* method for the determination of pesticide residues in
  food. *J. Off. Anal. Chem.* **59**, 169–171

  R. G. Staudte and S. J. Sheather (1990) *Robust Estimation and Testing.*

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ddt_kale.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ddt_kale.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/DDT.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ddt_kale.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
