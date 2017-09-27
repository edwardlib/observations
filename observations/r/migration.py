# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def migration(path):
  """Canadian Interprovincial Migration Data

  The `Migration` data frame has 90 rows and 8 columns.

  This data frame contains the following columns:

  source
      Province of origin (source). A factor with levels: `ALTA`,
      Alberta; `BC`, British Columbia; `MAN`, Manitoba; `NB`, New
      Brunswick; `NFLD`, New Foundland; `NS`, Nova Scotia; `ONT`,
      Ontario; `PEI`, Prince Edward Island; `QUE`, Quebec; `SASK`,
      Saskatchewan.

  destination
      Province of destination (1971 residence). A factor with levels:
      `ALTA`, Alberta; `BC`, British Columbia; `MAN`, Manitoba;
      `NB`, New Brunswick; `NFLD`, New Foundland; `NS`, Nova Scotia;
      `ONT`, Ontario; `PEI`, Prince Edward Island; `QUE`, Quebec;
      `SASK`, Saskatchewan.

  migrants
      Number of migrants (from source to destination) in the period
      1966–1971.

  distance
      Distance (between principal cities of provinces): NFLD, St. John;
      PEI, Charlottetown; NS, Halifax; NB, Fredricton; QUE, Montreal; ONT,
      Toronto; MAN, Winnipeg; SASK, Regina; ALTA, Edmonton; BC, Vancouver.

  pops66
      1966 population of source province.

  pops71
      1971 population of source province.

  popd66
      1966 population of destination province.

  popd71
      1971 population of destination province.

  Canada (1962) *Map*. Department of Mines and Technical Surveys.

  Canada (1971) *Census of Canada*. Statistics Canada, Vol. 1, Part 2
  [Table 32].

  Canada (1972) *Canada Year Book*. Statistics Canada [p. 1369].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `migration.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'migration.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Migration.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='migration.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
