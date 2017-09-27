# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def newpainters(path):
  """The Discretized Painter's Data of de Piles

  The original painters data contain the subjective assessment, on a 0 to
  20 integer scale, of 54 classical painters. The newpainters data
  discretizes the subjective assessment by quartiles with thresholds 25%,
  50%, 75%. The painters were assessed on four characteristics:
  composition, drawing, colour and expression. The data is due to the
  Eighteenth century art critic, de Piles.

  A table containing 5 variables ("Composition", "Drawing", "Colour",
  "Expression", and "School") and 54 observations.

  A. J. Weekes (1986).“A Genstat Primer”. Edward Arnold.

  M. Davenport and G. Studdert-Kennedy (1972). “The statistical analysis
  of aesthetic judgement: an exploration.” *Applied Statistics*, vol. 21,
  pp. 324–333.

  I. T. Jolliffe (1986) “Principal Component Analysis.” Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `newpainters.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 54 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'newpainters.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/newpainters.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='newpainters.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
