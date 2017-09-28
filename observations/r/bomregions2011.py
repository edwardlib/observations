# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bomregions2011(path):
  """Australian and Related Historical Annual Climate Data, by region

  Australian regional temperature data, Australian regional rainfall data,
  and Annual SOI, are given for the years 1900-2008 or 1900-2011 or
  1900-2012. The regional rainfall and temperature data are area-weighted
  averages for the respective regions. The Southern Oscillation Index
  (SOI) is the difference in barometric pressure at sea level between
  Tahiti and Darwin.

  This data frame contains the following columns:

  Year
      Year

  eastAVt
      Eastern temperature

  seAVt
      Southeastern region average temperature (degrees C)

  southAVt
      Southern temperature

  swAVt
      Southwestern temperature

  westAVt
      Western temperature

  northAVt
      Northern temperature

  mdbAVt
      Murray-Darling basin temperature

  auAVt
      Australian average temperature, area-weighted mean

  eastRain
      Eastern rainfall

  seRain
      Southeast Australian annual rainfall (mm)

  southRain
      Southern rainfall

  swRain
      Southwest rainfall

  westRain
      Western rainfall

  northRain
      Northern rainfall

  mdbRain
      Murray-Darling basin rainfall

  auRain
      Australian average rainfall, area weighted

  SOI
      Annual average Southern Oscillation Index

  co2mlo
      Moana Loa CO2 concentrations, from 1959

  co2law
      Moana Loa CO2 concentrations, 1900 to 1978

  CO2
      CO2 concentrations, composite series

  sunspot
      Annual average sunspot counts

  Australian Bureau of Meteorology web pages:

  http://www.bom.gov.au/climate/change/index.shtml

  The CO2 series `co2law`, for Law Dome ice core data. is from
  http://cdiac.ornl.gov/trends/co2/lawdome.html.

  The CO2 series `co2mlo` is from Dr. Pieter Tans, NOAA/ESRL
(`www.esrl.noaa.gov/gmd/ccgg/trends/ <www.esrl.noaa.gov/gmd/ccgg/trends/>`__)

  The series `CO2` is a composite series, obtained by adding 0.46 to he
  Law data for 1900 to 1958, then following this with the Moana Loa data
  that is avaiable from 1959. The addition of 0.46 is designed so that the
  averages from the two series agree for the period 1959 to 1968

  Sunspot data is from http://sidc.oma.be/sunspot-data/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bomregions2011.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 112 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bomregions2011.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/bomregions2011.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bomregions2011.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
