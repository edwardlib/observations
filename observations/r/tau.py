# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tau(path):
  """Tau Particle Decay Modes

  The `tau` data frame has 60 rows and 2 columns.

  The tau particle is a heavy electron-like particle discovered in the
  1970's by Martin Perl at the Stanford Linear Accelerator Center. Soon
  after its production the tau particle decays into various collections of
  more stable particles. About 86% of the time the decay involves just one
  charged particle. This rate has been measured independently 13 times.

  The one-charged-particle event is made up of four major modes of decay
  as well as a collection of other events. The four main types of decay
  are denoted rho, pi, e and mu. These rates have been measured
  independently 6, 7, 14 and 19 times respectively. Due to physical
  constraints each experiment can only estimate the composite
  one-charged-particle decay rate or the rate of one of the major modes of
  decay.

  Each experiment consists of a major research project involving many
  years work. One of the goals of the experiments was to estimate the rate
  of decay due to events other than the four main modes of decay. These
  are uncertain events and so cannot themselves be observed directly.

  This data frame contains the following columns:

  `rate`
      The decay rate expressed as a percentage.

  `decay`
      The type of decay measured in the experiment. It is a factor with
      levels `1`, `rho`, `pi`, `e` and `mu`.

  The data were obtained from

  Efron, B. (1992) Jackknife-after-bootstrap standard errors and influence
  functions (with Discussion). *Journal of the Royal Statistical Society,
  B*, **54**, 83–127.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tau.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tau.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/tau.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tau.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
