# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def plant_traits(path):
  """Plant Species Traits Data

  This dataset constitutes a description of 136 plant species according to
  biological attributes (morphological or reproductive)

  A data frame with 136 observations on the following 31 variables.

  `pdias`
      Diaspore mass (mg)

  `longindex`
      Seed bank longevity

  `durflow`
      Flowering duration

  `height`
      Plant height, an ordered factor with levels `1` < `2` < ... <
      `8`.

  `begflow`
      Time of first flowering, an ordered factor with levels `1` < `2`
      < `3` < `4` < `5` < `6` < `7` < `8` < `9`

  `mycor`
      Mycorrhizas, an ordered factor with levels `0`\ never < `1`
      sometimes< `2`\ always

  `vegaer`
      aerial vegetative propagation, an ordered factor with levels
      `0`\ never < `1` present but limited< `2`\ important.

  `vegsout`
      underground vegetative propagation, an ordered factor with 3 levels
      identical to `vegaer` above.

  `autopoll`
      selfing pollination, an ordered factor with levels `0`\ never <
      `1`\ rare < `2` often< the rule\ `3`

  `insects`
      insect pollination, an ordered factor with 5 levels `0` < ... <
      `4`.

  `wind`
      wind pollination, an ordered factor with 5 levels `0` < ... <
      `4`.

  `lign`
      a binary factor with levels `0:1`, indicating if plant is woody.

  `piq`
      a binary factor indicating if plant is thorny.

  `ros`
      a binary factor indicating if plant is rosette.

  `semiros`
      semi-rosette plant, a binary factor (`0`: no; `1`: yes).

  `leafy`
      leafy plant, a binary factor.

  `suman`
      summer annual, a binary factor.

  `winan`
      winter annual, a binary factor.

  `monocarp`
      monocarpic perennial, a binary factor.

  `polycarp`
      polycarpic perennial, a binary factor.

  `seasaes`
      seasonal aestival leaves, a binary factor.

  `seashiv`
      seasonal hibernal leaves, a binary factor.

  `seasver`
      seasonal vernal leaves, a binary factor.

  `everalw`
      leaves always evergreen, a binary factor.

  `everparti`
      leaves partially evergreen, a binary factor.

  `elaio`
      fruits with an elaiosome (dispersed by ants), a binary factor.

  `endozoo`
      endozoochorous fruits, a binary factor.

  `epizoo`
      epizoochorous fruits, a binary factor.

  `aquat`
      aquatic dispersal fruits, a binary factor.

  `windgl`
      wind dispersed fruits, a binary factor.

  `unsp`
      unspecialized mechanism of seed dispersal, a binary factor.

  Vallet, Jeanne (2005) *Structuration de communautés végétales et analyse
  comparative de traits biologiques le long d'un gradient d'urbanisation*.
  Mémoire de Master 2 'Ecologie-Biodiversité-Evolution'; Université Paris
  Sud XI, 30p.+ annexes (in french)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `plant_traits.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 136 rows and 31 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'plant_traits.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/plantTraits.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='plant_traits.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
