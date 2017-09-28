# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kiwishade(path):
  """Kiwi Shading Data

  The `kiwishade` data frame has 48 rows and 4 columns. The data are
  from a designed experiment that compared different kiwifruit shading
  treatments. There are four vines in each plot, and four plots (one for
  each of four treatments: none, Aug2Dec, Dec2Feb, and Feb2May) in each of
  three blocks (locations: west, north, east). Each plot has the same
  number of vines, each block has the same number of plots, with each
  treatment occurring the same number of times.

  This data frame contains the following columns:

  yield
      Total yield (in kg)

  plot
      a factor with levels `east.Aug2Dec`, `east.Dec2Feb`,
      `east.Feb2May`, `east.none`, `north.Aug2Dec`,
      `north.Dec2Feb`, `north.Feb2May`, `north.none`,
      `west.Aug2Dec`, `west.Dec2Feb`, `west.Feb2May`, `west.none`

  block
      a factor indicating the location of the plot with levels `east`,
      `north`, `west`

  shade
      a factor representing the period for which the experimenter placed
      shading over the vines; with levels: `none` no shading,
      `Aug2Dec` August - December, `Dec2Feb` December - February,
      `Feb2May` February - May

  Snelgar, W.P., Manson. P.J., Martin, P.J. 1992. Influence of time of
  shading on flowering and yield of kiwifruit vines. Journal of
  Horticultural Science 67: 481-487.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kiwishade.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kiwishade.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/kiwishade.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kiwishade.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
