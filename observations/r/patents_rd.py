# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def patents_rd(path):
  """Patents, R\\&D and Technological Spillovers for a Panel of Firms

  a panel of 181 observations from 1983 to 1991

  *number of observations* : 1629

  *observation* : production units

  *country* : world

  A dataframe containing :

  year
      year

  fi
      firm's id

  sector
      firm's main industry sector, one of aero (aerospace), chem
      (chemistry), comput (computer), drugs, elec (electricity), food,
      fuel (fuel and mining), glass, instr (instruments), machin
      (machinery), metals, other, paper, soft (software), motor (motor
      vehicles)

  geo
      geographic area, one of eu (European Union), japan, usa, rotw (rest
      of the world)

  patent
      numbers of European patent applications

  rdexp
      log of R\\&D expenditures

  spil
      log of spillovers

  Cincer, Michele (1997) “Patents, R \\& D and technological spillovers at
  the firm level : some evidence from econometric count models for panel
  data”, *Journal of Applied Econometrics*, **12(3)**, may–june, 265–280.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `patents_rd.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1629 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'patents_rd.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/PatentsRD.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='patents_rd.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
