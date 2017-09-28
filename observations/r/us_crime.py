# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_crime(path):
  """The Effect of Punishment Regimes on Crime Rates

  Criminologists are interested in the effect of punishment regimes on
  crime rates. This has been studied using aggregate data on 47 states of
  the USA for 1960 given in this data frame. The variables seem to have
  been re-scaled to convenient numbers.

  This data frame contains the following columns:

  `M`
      percentage of males aged 14–24.

  `So`
      indicator variable for a Southern state.

  `Ed`
      mean years of schooling.

  `Po1`
      police expenditure in 1960.

  `Po2`
      police expenditure in 1959.

  `LF`
      labour force participation rate.

  `M.F`
      number of males per 1000 females.

  `Pop`
      state population.

  `NW`
      number of non-whites per 1000 people.

  `U1`
      unemployment rate of urban males 14–24.

  `U2`
      unemployment rate of urban males 35–39.

  `GDP`
      gross domestic product per head.

  `Ineq`
      income inequality.

  `Prob`
      probability of imprisonment.

  `Time`
      average time served in state prisons.

  `y`
      rate of crimes in a particular category per head of population.

  Ehrlich, I. (1973) Participation in illegitimate activities: a
  theoretical and empirical investigation. *Journal of Political Economy*,
  **81**, 521–565.

  Vandaele, W. (1978) Participation in illegitimate activities: Ehrlich
  revisited. In *Deterrence and Incapacitation*, eds A. Blumstein, J.
  Cohen and D. Nagin, pp. 270–335. US National Academy of Sciences.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_crime.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 47 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_crime.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/UScrime.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_crime.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
