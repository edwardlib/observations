# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cholera(path):
  """William Farr's Data on Cholera in London, 1849

  In 1852, William Farr, published a report of the Registrar-General on
  mortality due to cholera in England in the years 1848-1849, during which
  there was a large epidemic throughout the country. Farr initially
  believed that cholera arose from bad air ("miasma") associated with low
  elevation above the River Thames. John Snow (1855) later showed that the
  disease was principally spread by contaminated water.

  This data set comes from a paper by Brigham et al. (2003) that analyses
  some tables from Farr's report to examine the prevalence of death from
  cholera in the districts of London in relation to the available
  predictors from Farr's table.

  A data frame with 38 observations on the following 15 variables.

  `district`
      name of the district in London, a character vector

  `cholera_drate`
      deaths from cholera in 1849 per 10,000 inhabitants, a numeric vector

  `cholera_deaths`
      number of deaths registered from cohlera in 1849, a numeric vector

  `popn`
      population, in the middle of 1849, a numeric vector

  `elevation`
      elevation, in feet above the high water mark, a numeric vector

  `region`
      a grouping of the London districts, a factor with levels `West`
      `North` `Central` `South` `Kent`

  `water`
      water supply region, a factor with levels `Battersea`
      `New River` `Kew`; see Details

  `annual_deaths`
      annual deaths from all causes, 1838-1844, a numeric vector

  `pop_dens`
      population density (persons per acre), a numeric vector

  `persons_house`
      persons per inhabited house, a numeric vector

  `house_valpp`
      average annual value of house, per person (pounds), a numeric vector

  `poor_rate`
      poor rate precept per pound of howse value, a numeric vector

  `area`
      district area, a numeric vector

  `houses`
      number of houses, a numeric vector

  `house_val`
      total house values, a numeric vector

  Bingham P., Verlander, N. Q., Cheal M. J. (2004). John Snow, William
  Farr and the 1849 outbreak of cholera that affected London: a reworking
  of the data highlights the importance of the water supply. *Public
  Health*, 118(6), 387-394, Table 2. (The data was kindly supplied by
  Neville Verlander, including additional variables not shown in their
  Table 2.)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cholera.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cholera.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Cholera.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cholera.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
