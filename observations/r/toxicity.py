# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def toxicity(path):
  """Toxicity of Carboxylic Acids Data

  The aim of the experiment was to predict the toxicity of carboxylic
  acids on the basis of several molecular descriptors.

  A data frame with 38 observations on the following 10 variables which
  are attributes for carboxylic acids:

  `toxicity`
      aquatic toxicity, defined as *log(IGC50^(-1))*; typically the
      “response”.

  `logKow`
      *log Kow*, the partition coefficient

  `pKa`
      pKa: the dissociation constant

  `ELUMO`
      **E**\ nergy of the **l**\ owest **u**\ noccupied **m**\ olecular
      **o**\ rbital

  `Ecarb`
      Electrotopological state of the **carb**\ oxylic group

  `Emet`
      Electrotopological state of the **met**\ hyl group

  `RM`
      Molar refractivity

  `IR`
      Refraction index

  `Ts`
      Surface tension

  `P`
      Polarizability

  The website accompanying the MMY-book:
  http://www.wiley.com/legacy/wileychi/robust_statistics

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `toxicity.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'toxicity.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/toxicity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='toxicity.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
