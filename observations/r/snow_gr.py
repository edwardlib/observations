# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def snow_gr(path):
  """Snowfall data for Grand Rapids, MI

  Official snowfall data by month and season for Grand Rapids, MI, going
  back to 1893.

  A data frame with 119 observations of the following variables.

  -  `SeasonStart` Year in which season started (July is start of
     season)

  -  `SeasonEnd` Year in which season ended (June is end of season)

  -  `Jul` Inches of snow in July

  -  `Aug` Inches of snow in August

  -  `Sep` Inches of snow in September

  -  `Oct` Inches of snow in October

  -  `Nov` Inches of snow in November

  -  `Dec` Inches of snow in December

  -  `Jan` Inches of snow in January

  -  `Feb` Inches of snow in February

  -  `Mar` Inches of snow in March

  -  `Apr` Inches of snow in April

  -  `May` Inches of snow in May

  -  `Jun` Inches of snow in June

  -  `Total` Inches of snow for entire season (July-June)

  These data were compiled by Laura Kapitula from data available at
  http://www.crh.noaa.gov/grr/climate/data/grr/snowfall/.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `snow_gr.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 119 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'snow_gr.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/SnowGR.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='snow_gr.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
