# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def biomass_till(path):
  """Biomass Tillage Data

  An agricultural experiment in which different tillage methods were
  implemented. The effects of tillage on plant (maize) biomass were
  subsequently determined by modeling biomass accumulation for each
  tillage treatment using a 3 parameter Weibull function.

  A datset where the total biomass is modeled conditional on a three value
  factor, and hence *vector* parameters are used.

  A data frame with 58 observations on the following 3 variables.

  `Tillage`
      Tillage treatments, a `factor` with levels

      `CA-`:
          a no-tillage system with plant residues removed

      `CA+`:
          a no-tillage system with plant residues retained

      `CT`:
          a conventionally tilled system with residues incorporated

  `DVS`
      the development stage of the maize crop. A DVS of `1` represents
      maize anthesis (flowering), and a DVS of `2` represents
      physiological maturity. For the data, numeric vector with 5
      different values between 0.5 and 2.

  `Biomass`
      accumulated biomass of maize plants from each tillage treatment.

  `Biom.2`
      the same as `Biomass`, but with three values replaced by “gross
      errors”.

  From Strahinja Stepanovic and John Laborde, Department of Agronomy &
  Horticulture, University of Nebraska-Lincoln, USA

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `biomass_till.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 58 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'biomass_till.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/biomassTill.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='biomass_till.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
