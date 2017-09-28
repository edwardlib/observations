# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def painters(path):
  """The Painter's Data of de Piles

  The subjective assessment, on a 0 to 20 integer scale, of 54 classical
  painters. The painters were assessed on four characteristics:
  composition, drawing, colour and expression. The data is due to the
  Eighteenth century art critic, de Piles.

  The row names of the data frame are the painters. The components are:

  `Composition`
      Composition score.

  `Drawing`
      Drawing score.

  `Colour`
      Colour score.

  `Expression`
      Expression score.

  `School`
      The school to which a painter belongs, as indicated by a factor
      level code as follows: `"A"`: Renaissance; `"B"`: Mannerist;
      `"C"`: Seicento; `"D"`: Venetian; `"E"`: Lombard; `"F"`:
      Sixteenth Century; `"G"`: Seventeenth Century; `"H"`: French.

  A. J. Weekes (1986) *A Genstat Primer.* Edward Arnold.

  M. Davenport and G. Studdert-Kennedy (1972) The statistical analysis of
  aesthetic judgement: an exploration. *Applied Statistics* **21**,
  324–333.

  I. T. Jolliffe (1986) *Principal Component Analysis.* Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `painters.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 54 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'painters.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/painters.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='painters.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
