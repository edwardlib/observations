from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gilgais(path):
  """Line Transect of Soil in Gilgai Territory

  This dataset was collected on a line transect survey in gilgai territory
  in New South Wales, Australia. Gilgais are natural gentle depressions in
  otherwise flat land, and sometimes seem to be regularly distributed. The
  data collection was stimulated by the question: are these patterns
  reflected in soil properties? At each of 365 sampling locations on a
  linear grid of 4 meters spacing, samples were taken at depths 0-10 cm,
  30-40 cm and 80-90 cm below the surface. pH, electrical conductivity and
  chloride content were measured on a 1:5 soil:water extract from each
  sample.

  This data frame contains the following columns:

  `pH00`
      pH at depth 0–10 cm.

  `pH30`
      pH at depth 30–40 cm.

  `pH80`
      pH at depth 80–90 cm.

  `e00`
      electrical conductivity in mS/cm (0–10 cm).

  `e30`
      electrical conductivity in mS/cm (30–40 cm).

  `e80`
      electrical conductivity in mS/cm (80–90 cm).

  `c00`
      chloride content in ppm (0–10 cm).

  `c30`
      chloride content in ppm (30–40 cm).

  `c80`
      chloride content in ppm (80–90 cm).

  Webster, R. (1977) Spectral analysis of gilgai soil. *Australian Journal
  of Soil Research* **15**, 191–204.

  Laslett, G. M. (1989) Kriging and splines: An empirical comparison of
  their predictive performance in some applications (with discussion).
  *Journal of the American Statistical Association* **89**, 319–409

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gilgais.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 365 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gilgais.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/MASS/gilgais.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gilgais.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
