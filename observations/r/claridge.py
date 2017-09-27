# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def claridge(path):
  """Genetic Links to Left-handedness

  The `claridge` data frame has 37 rows and 2 columns.

  The data are from an experiment which was designed to look for a
  relationship between a certain genetic characteristic and handedness.
  The 37 subjects were women who had a son with mental retardation due to
  inheriting a defective X-chromosome. For each such mother a genetic
  measurement of their DNA was made. Larger values of this measurement are
  known to be linked to the defective gene and it was hypothesized that
  larger values might also be linked to a progressive shift away from
  right-handednesss. Each woman also filled in a questionnaire regarding
  which hand they used for various tasks. From these questionnaires a
  measure of hand preference was found for each mother. The scale of this
  measure goes from 1, indicating someone who always favours their right
  hand, to 8, indicating someone who always favours their left hand.
  Between these two extremes are people who favour one hand for some tasks
  and the other for other tasks.

  This data frame contains the following columns:

  `dnan`
      The genetic measurement on each woman's DNA.

  `hand`
      The measure of left-handedness on an integer scale from 1 to 8.

  The data were kindly made available by Dr. Gordon S. Claridge from the
  Department of Experimental Psychology, University of Oxford.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `claridge.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'claridge.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/claridge.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='claridge.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
