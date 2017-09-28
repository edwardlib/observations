# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def armada(path):
  """La Felicisima Armada

  The Spanish Armada (Spanish: *Grande y Felicisima Armada*, literally
  "Great and Most Fortunate Navy") was a Spanish fleet of 130 ships that
  sailed from La Coruna in August 1588. During its preparation, several
  accounts of its formidable strength were circulated to reassure allied
  powers of Spain or to intimidate its enemies. One such account was given
  by Paz Salas et Alvarez (1588). The intent was bring the forces of Spain
  to invade England, overthrow Queen Elizabeth I, and re-establish Spanish
  control of the Netherlands. However the Armada was not as fortunate as
  hoped: it was all destroyed in one week's fighting.

  de Falguerolles (2008) reports the table given here as `Armada` as an
  early example of data to which multivariate methods might be applied.

  A data frame with 10 observations on the following 11 variables.

  `Armada`
      designation of the fleet, a factor with levels `Andalucia`
      `Castilla` `Galeras` `Guipuscua` `Napoles` `Pataches`
      `Portugal` `Uantiscas` `Vizca` `Vrcas`

  `ships`
      number of ships, a numeric vector

  `tons`
      total tons, a numeric vector

  `soldiers`
      number of soldiers, a numeric vector

  `sailors`
      number of sailors, a numeric vector

  `men`
      total of soldiers plus sailors, a numeric vector

  `artillery`
      a numeric vector

  `balls`
      a numeric vector

  `gunpowder`
      a numeric vector

  `lead`
      a numeric vector

  `rope`
      a numeric vector

  de Falguerolles, A. (2008) L'analyse des donnees; before and around.
  *Journal Electronique d'Histoire des Probabilites et de la Statistique*,
  4 (2),
`www.jehps.net/Decembre2008/Falguerolles.pdf <www.jehps.net/Decembre2008/Falg
  uerolles.pdf>`__

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `armada.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'armada.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Armada.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='armada.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
