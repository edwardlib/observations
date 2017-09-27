# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ambient_noxch(path):
  """Daily Means of NOx (mono-nitrogen oxides) in air

  This dataset contains daily means (from midnight to midnight) of NOx,
  i.e., mono-nitrogen oxides, in [ppb] at 13 sites in central Switzerland
  and Aarau for the year 2004.

  A data frame with 366 observations on the following 14 variables.

  `date`
      date of day, of class `"Date"`.

  `ad`
      Site is located north of Altdorf 100 meters east of motorway A2, on
      an open field at the beginning of a more than 2000m deep valley
      (690.175, 193.55; 438; inLuft)

  `ba`
      Site is located in the centre of the little town of Baden in a
      residential area. Baden has 34'000 inhabitants and is situated on
      the swiss plateau (666.075, 257.972; 377; inLuft).

  `ef`
      Site is located 6 km south of altdorf and 800 m north of the village
      of Erstfeld. The motorway A2 passes 5 m west of the measuring site.
      Over 8 million vehicles have passed Erstfeld in 2004 where 13% of
      the counts were attributed to trucks (691.43, 187.69; 457; MFM-U).

  `la`
      Site is located on a wooded hill in a rural area called Laegern,
      about 190 m above Baden, which is about 5 km away (669.8, 259; 690;
      NABEL).

  `lu`
      Site is located in the center of town of Lucerne, which has 57'000
      inhabitants (666.19, 211.975; 460; inLuft).

  `re`
      Site is located 1 km west of Reiden on the Swiss plateau. The
      motorway A2 passes 5 m west of the measuring site (639.56, 232.11;
      462; MFM-U).

  `ri`
      Site is located at Rigi Seebodenalp, 649 m above the lake of Lucerne
      on an alp with half a dozen small houses (677.9, 213.5; 1030;
      NABEL).

  `se`
      Site is located in Sedel next to town of Lucerne 35m above and 250m
      south of motorway A14 from Zug to Lucerne on a low hill with free
      360° panorama (665.5, 213.41; 484; inLuft).

  `si`
      Site is located at the border of a small industrial area in Sisseln,
      300 m east of a main road (640.725, 266.25; 305; inLuft).

  `st`
      Site is located at the south east border of Stans with 7'000
      inhabitants (670.85, 201.025; 438; inLuft).

  `su`
      Site is located in the center of Suhr (8700 inhabitants), 10 m from
      the main road (648.49, 246.985; 403; inLuft).

  `sz`
      Site is located in Schwyz (14'200 inhabitants) near a shopping
      center (691.92, 208.03; 470; inLuft).

  `zg`
      Site is located in the centre of Zug with 22'000 inhabitants, 24 m
      from the main road (681.625, 224.625; 420; inLuft).

  | http://www.in-luft.ch/
  | http://www.empa.ch/plugin/template/empa/\*/6794
  | http://www.bafu.admin.ch/umweltbeobachtung/02272/02280

  See Also
  ~~~~~~~~

  another NOx dataset, `NOxEmissions`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ambient_noxch.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 366 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ambient_noxch.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/ambientNOxCH.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ambient_noxch.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
