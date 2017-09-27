# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def waders(path):
  """Counts of Waders at 15 Sites in South Africa

  The `waders` data frame has 15 rows and 19 columns. The entries are
  counts of waders in summer.

  This data frame contains the following columns (species)

  `S1`
      Oystercatcher

  `S2`
      White-fronted Plover

  `S3`
      Kitt Lutz's Plover

  `S4`
      Three-banded Plover

  `S5`
      Grey Plover

  `S6`
      Ringed Plover

  `S7`
      Bar-tailed Godwit

  `S8`
      Whimbrel

  `S9`
      Marsh Sandpiper

  `S10`
      Greenshank

  `S11`
      Common Sandpiper

  `S12`
      Turnstone

  `S13`
      Knot

  `S14`
      Sanderling

  `S15`
      Little Stint

  `S16`
      Curlew Sandpiper

  `S17`
      Ruff

  `S18`
      Avocet

  `S19`
      Black-winged Stilt

  The rows are the sites:

  | A = Namibia North coast
  | B = Namibia North wetland
  | C = Namibia South coast
  | D = Namibia South wetland
  | E = Cape North coast
  | F = Cape North wetland
  | G = Cape West coast
  | H = Cape West wetland
  | I = Cape South coast
  | J= Cape South wetland
  | K = Cape East coast
  | L = Cape East wetland
  | M = Transkei coast
  | N = Natal coast
  | O = Natal wetland

  J.C. Gower and D.J. Hand (1996) *Biplots* Chapman & Hall Table 9.1.
  Quoted as from:

  R.W. Summers, L.G. Underhill, D.J. Pearson and D.A. Scott (1987) Wader
  migration systems in south and eastern Africa and western Asia. *Wader
  Study Group Bulletin* **49** Supplement, 15–34.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `waders.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'waders.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/waders.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='waders.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
