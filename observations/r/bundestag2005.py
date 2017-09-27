# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bundestag2005(path):
  """Votes in German Bundestag Election 2005

  Number of votes by province in the German Bundestag election 2005 (for
  the parties that eventually entered the parliament).

  A 2-way `"table"` giving the number of votes for each party
  (`Fraktion`) in each of the 16 German provinces (`Bundesland`):

  +------+--------------+---------------------------------------------------+
  | No   | Name         | Levels                                            |
  +------+--------------+---------------------------------------------------+
  | 1    | Bundesland   | Schleswig-Holstein, Mecklenburg-Vorpommern, ...   |
  +------+--------------+---------------------------------------------------+
  | 2    | Fraktion     | SPD, CDU/CSU, Gruene, FDP, Linke                  |
  +------+--------------+---------------------------------------------------+

  Der Bundeswahlleiter, Statistisches Bundesamt.
http://www.bundeswahlleiter.de/de/bundestagswahlen/fruehere_bundestagswahlen/
  btw2005.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bundestag2005.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bundestag2005.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Bundestag2005.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bundestag2005.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
