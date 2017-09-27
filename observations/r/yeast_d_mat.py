# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def yeast_d_mat(path):
  """Student's (1906) Yeast Cell Counts

  Counts of the number of yeast cells were made each of 400 regions in a
  20 x 20 grid on a microscope slide, comprising a 1 sq. mm. area. This
  experiment was repeated four times, giving samples A, B, C and D.

  Student (1906) used these data to investigate the errors in random
  sampling. He says "there are two sources of error: (a) the drop taken
  may not be representative of the bulk of the liquid; (b) the
  distribution of the cells over the area which is examined is never
  exactly uniform, so that there is an 'error of random sampling.'"

  The data in the paper are provided in the form of discrete frequency
  distributions for the four samples. Each shows the frequency
  distribution squares containing a `count` of 0, 1, 2, ... yeast cells.
  These are combined here in `Yeast`. In addition, he gives a table
  (Table I) showing the actual number of yeast cells counted in the 20 x
  20 grid for sample D, given here as `YeastD.mat`.

  `Yeast`: A frequency data frame with 36 observations on the following
  3 variables, giving the frequencies of

  `sample`
      Sample identifier, a factor with levels `A` `B` `C` `D`

  `count`
      The number of yeast cells counted in a square

  `freq`
      The number of squares with the given `count`

  `YeastD.mat`: A 20 x 20 matrix containing the count of yeast cells in
  each square for sample D.

  D. J. Hand, F. Daly, D. Lunn, K. McConway and E. Ostrowski (1994). *A
  Handbook of Small Data Sets*. London: Chapman \\& Hall. The data may be
  found at:
  http://www.stat.duke.edu/courses/Spring98/sta113/Data/Hand/yeast.dat

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `yeast_d_mat.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'yeast_d_mat.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/YeastD.mat.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='yeast_d_mat.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
