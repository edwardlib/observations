# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wheat_monarchs(path):
  """Playfair's Data on Wages and the Price of Wheat

  Playfair (1821) used a graph, showing parallel time-series of the price
  of wheat and the typical weekly wage for a "good mechanic" from 1565 to
  1821 to argue that working men had never been as well-off in terms of
  purchasing power as they had become toward the end of this period.

  His graph is a classic in the history of data visualization, but commits
  the sin of showing two non-commensurable Y variables on different axes.
  Scatterplots of wages vs. price or plots of ratios (e.g., wages/price)
  are in some ways better, but both of these ideas were unknown in 1821.

  In this version, information on the reigns of British monarchs is
  provided in a separate data.frame, `Wheat.monarch`.

  `Wheat` A data frame with 53 observations on the following 3
  variables.

  `Year`
      Year, in intervals of 5 from 1565 to 1821: a numeric vector

  `Wheat`
      Price of Wheat (Shillings/Quarter bushel): a numeric vector

  `Wages`
      Weekly wage (Shillings): a numeric vector

  `Wheat.monarchs` A data frame with 12 observations on the following 4
  variables.

  `name`
      Reigning monarch, a factor with levels `Anne` `Charles I`
      `Charles II` `Cromwell` `Elizabeth` `George I` `George II`
      `George III` `George IV` `James I` `James II` `W&M`

  `start`
      Starting year of reign, a numeric vector

  `end`
      Starting year of reign, a numeric vector

  `commonwealth`
      A binary variable indicating the period of the Commonwealth under
      Cromwell

  Playfair, W. (1821). *Letter on our Agricultural Distresses, Their
  Causes and Remedies*. London: W. Sams, 1821

  Data values: originally digitized from
  http://www.math.yorku.ca/SCS/Gallery/images/playfair-wheat1.gif now
  taken from http://mbostock.github.com/protovis/ex/wheat.js

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wheat_monarchs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wheat_monarchs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Wheat.monarchs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wheat_monarchs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
