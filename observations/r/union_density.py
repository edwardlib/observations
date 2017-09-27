# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def union_density(path):
  """cross national rates of trade union density

  Cross-national data on relative size of the trade unions and predictors,
  in 20 countries. Two of the predictors are highly collinear, and are the
  source of a debate between Stephens and Wallerstein (1991), later
  reviewed by Western and Jackman (1994).

  -  `union`\ numeric, percentage of the total number of wage and salary
     earners plus the unemployed who are union members, measured between
     1975 and 1980, with most of the data drawn from 1979

  -  `left`\ numeric, an index tapping the extent to which parties of
     the left have controlled governments since 1919, due to Wilensky
     (1981).

  -  `size`\ numeric, log of labor force size, defined as the number of
     wage and salary earners, plus the unemployed

  -  `concen`\ numeric, percentage of employment, shipments, or
     production accounted for by the four largest enterprises in a
     particular industry, averaged over industries (with weights
     proportional to the size of the industry) and the resulting measure
     is normalized such that the United States scores a 1.0, and is due to
     Pryor (1973). Some of the scores on this variable are imputed using
     procedures described in Stephens and Wallerstein (1991, 945).

  Pryor, Frederic. 1973. *Property and Industrial Organization in
  Communist and Capitalist Countries*. Bloomington: Indiana University
  Press.

  Stephens, John and Michael Wallerstein. 1991. Industrial Concentration,
  Country Size and Trade Union Membership. *American Political Science
  Review* 85:941-953.

  Western, Bruce and Simon Jackman. 1994. Bayesian Inference for
  Comparative Research. *American Political Science Review* 88:412-423.

  Wilensky, Harold L. 1981. Leftism, Catholicism, Democratic Corporatism:
  The Role of Political Parties in Recemt Welfare State Development. In
  *The Development of Welfare States in Europe and America*, ed. Peter
  Flora and Arnold J. Heidenheimer. New Brunswick: Transaction Books.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `union_density.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'union_density.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/unionDensity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='union_density.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
