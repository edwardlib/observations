# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def paulsen(path):
  """Neurotransmission in Guinea Pig Brains

  The `paulsen` data frame has 346 rows and 1 columns.

  Sections were prepared from the brain of adult guinea pigs. Spontaneous
  currents that flowed into individual brain cells were then recorded and
  the peak amplitude of each current measured. The aim of the experiment
  was to see if the current flow was quantal in nature (i.e. that it is
  not a single burst but instead is built up of many smaller bursts of
  current). If the current was indeed quantal then it would be expected
  that the distribution of the current amplitude would be multimodal with
  modes at regular intervals. The modes would be expected to decrease in
  magnitude for higher current amplitudes.

  This data frame contains the following column:

  `y`
      The current flowing into individual brain cells. The currents are
      measured in pico-amperes.

  The data were kindly made available by Dr. O. Paulsen from the
  Department of Pharmacology at the University of Oxford.

  Paulsen, O. and Heggelund, P. (1994) The quantal size at
  retinogeniculate synapses determined from spontaneous and evoked EPSCs
  in guinea-pig thalamic slices. *Journal of Physiology*, **480**,
  505–511.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `paulsen.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 346 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'paulsen.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/paulsen.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='paulsen.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
