# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def terrorism(path):
  """Global Terrorism Database yearly summaries

  The `Global Terrorism Database
  (GTD) <https://en.wikipedia.org/wiki/Global_Terrorism_Database>`__ "is a
  database of incidents of terrorism from 1970 onward". Through 2015, this
  database contains information on 141,966 incidents.

  `terrorism` provides a few summary statistics along with an
  `ordered` factor `methodology`, which `Pape et
al. <https://www.washingtonpost.com/news/monkey-cage/wp/2014/08/11/how-to-fix
  -the-flaws-in-the-global-terrorism-database-and-why-it-matters/>`__
  insisted is necessary, because an increase of over 70 percent in suicide
  terrorism between 2007 and 2013 is best explained by a methodology
  change in GTD that occurred on 2011-11-01; Pape's own `Suicide Attack
  Database <https://en.wikipedia.org/wiki/Suicide_Attack_Database>`__
  showed a 19 percent *decrease* over the same period.

  `incidents.byCountryYr` and `nkill.byCountryYr` are matrices giving
  the numbes of incidents and numbers of deaths by year and by country for
  206 countries and for all years between 1970 and 2015 except for 1993,
  for which the raw data were lost.

  NOTE: For nkill.byCountryYr and for terrorism[c('nkill', 'nkill.us')],
  NAs in GTD were treated as 0. Thus the actual number of deaths were
  likely higher, unless this was more than offset by incidents being
  classified as terrorism, when they should not have been.

  `terrorism` is a `data.frame` containing the following:

  year
      integer year, 1970:2014.

  methodology
      an `ordered` factor giving the methodology / organization
      responsible for the data collection for most of the given year. The
      Pinkerton Global Intelligence Service (PGIS) managed data collection
      from 1970-01-01 to 1997-12-31. The Center for Terrorism and
      Intelligence Studies (CETIS) managed the project from 1998-01-01 to
      2008-03-31. The Institute for the Study of Violent Groups (ISVG)
      carried the project from 2008-04-01 to 2011-10-31. The National
      Consortium for the Study of Terrorism and Responses to Terrorism
      (START) has managed data collection since 2011-11-01. For this
      variable, partial years are ignored, so `methodology` = CEDIS for
      1998:2007, ISVG for 2008:2011, and START for 2012:2014.

  method
      a character vector consisting of the first character of the levels
      of `methodology`:

      c('p', 'c', 'i', 's')

  incidents
      integer number of incidents identified each year.

      NOTE: `sum(terrorism[["incidents"]])` = 146920 = 141966 in the GTD
      database plus 4954 for 1993, for which the incident-level data were
      lost.

  incidents.us
      integer number of incidents identified each year with
      `country_txt` = "United States".

  suicide
      integer number of incidents classified as "suicide" by GTD variable
      `suicide` = 1. For 2007, this is 359, the number reported by `Pape
      et
    al. <https://www.washingtonpost.com/news/monkey-cage/wp/2014/08/11/how-to
  -fix-the-flaws-in-the-global-terrorism-database-and-why-it-matters/>`__
      For 2013, it is 624, which is 5 more than the 619 mentioned by Pape
      et al. Without checking with the SMART project administrators, one
      might suspect that 5 more suicide incidents from 2013 were found
      after the data Pape et al. analyzed but before the data used for
      this analysis.

  suicide.us
      Number of suicide incidents by year with `country_txt` = "United
      States".

  nkill
      number of confirmed fatalities for incidents in the given year,
      including attackers = `sum(nkill, na.rm=TRUE)` in the GTD incident
      data.

      NOTE: `nkill` in the GTD incident data includes both perpetrators
      and victims when both are available. It includes one when only one
      is available and is `NA` when neither is available. However, in
      most cases, we might expect that the more spectacular and lethal
      incidents would likely be more accurately reported. To the exent
      that this is true, it means that when numbers are missing, they are
      usually zero or small. This further suggests that the summary
      numbers recorded here probably represent a slight but not
      substantive undercount.

  nkill.us
      number of U.S. citizens who died as a result of incidents for that
      year = `sum(nkill.us, na.rm=TRUE)` in the GTD incident data. (This
      is subject to the same likely modest undercount discussed with
      `nkill`.)

  nwound
      number of people wounded. (This is subject to the same likely modest
      undercount discussed with `nkill`.)

  nwound.us
      Number of U.S. citizens wounded in terrorist incidents for that year
      = `sum(nwound.us, na.rm=TRUE)` in the GTD incident data. (This is
      subject to the same likely modest undercount discussed with
      `nkill`.)

  pNA.nkill, pNA.nkill.us, pNA.nwound, pNA.nwound.us
      proportion of observations by year with missing values. These
      numbers are higher for the early data than more recent numbers. This
      is particularly true for `nkill.us` and `nwound.us`, which
      exceed 90 percent for most of the period with `methodology` =
      'PGIS', prior to 1998.

  worldPopulation, USpopulation
      Estimated de facto population in thousands living in the world and
      in the US as of 1 July of the year indicated, according to the
      Population Division of the Department of Economic and Social Affairs
      of the United Nations; see "Sources" below.

  worldDeathRate, USdeathRate
      `Crude death rate <https://en.wikipedia.org/wiki/Mortality_rate>`__
      (deaths per 1,000 population) worldwide and in the US, according to
      the World Bank; see "Sources" below. This World Bank data set
      includes USdeathRate for each year from 1900 to 2014.

      The WorldDeathRate here were read manually from a plot on `that web
    page, <http://data.worldbank.org/indicator/SP.DYN.CDRT.IN?end=2014&start=
  1960&view=chart>`__
      except for the the number for 2015, which was estimated as a
      reduction of 0.73 percent from 2014, which was the average rate of
      decline (ratio of two successive years) for 1990 to 2014. The same
      method was used to estimate the USdeathRate for 2015 as the same as
      for 2014.

      NOTE: USdeathRate is to two significant digits only, unlike
      WorldDeathRate, which has four significant digits.

  worldDeaths, USdeaths
      number of deaths by year in the world and US

      worldDeaths = worldPopulation \* worldDeathRate.

      USdeaths were computed by summing across age groups in
      "Deaths\_5x1.txt" for the United States, downloaded from
      http://www.mortality.org/cgi-bin/hmd/country.php?cntr=USA&level=1
      from the Human Mortality Database; see sources below.

  kill.pmp, kill.pmp.us
      terrorism deaths per million population worldwide and in the US =

      0.001 \* nkill / worldPopulation

  pkill, pkill.us
      terrorism deaths as a proportion of total deaths worldwide and in
      the US

      pkill = nkill / worldDeaths

      pkill.us = nkill.us / USdeaths

  The `Global Terrorism
  Database <https://en.wikipedia.org/wiki/Global_Terrorism_Database>`__
  maintained by the `National Consortium for the Study of Terrorism and
  Responses to
Terrorism <https://en.wikipedia.org/wiki/National_Consortium_for_the_Study_of
  _Terrorism_and_Responses_to_Terrorism>`__
  (START, 2015), `downloaded 2015-11-28 <http://www.start.umd.edu/gtd>`__.

  The world and US population figures came from `"Total Population - Both
  Sexes", World Population Prospects 2015, published by the Population
  Division of the Department of Economic and Social Affairs of the United
  Nations <https://esa.un.org/unpd/wpp/Download/Standard/Population/>`__,
  accessed 2016-09-05.

  The World and US death rates came from `the World
  Bank <http://data.worldbank.org/indicator/SP.DYN.CDRT.IN>`__, accessed
  2016-09-05.

  `Human Mortality Database. University of California, Berkeley (USA), and
  Max Planck Institute for Demographic Research
  (Germany). <http://www.mortality.org/>`__

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `terrorism.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 46 rows and 25 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'terrorism.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/terrorism.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='terrorism.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
