# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def income_inequality(path):
  """Income Inequality in the US

  Data on quantiles of the distributions of family incomes in the United
  States. This combines three data sources:

  (1) US Census Table F-1 for the central quantiles

  (2) Piketty and Saez for the 95th and higher quantiles

  (3) Gross Domestic Product and implicit price deflators from
  `MeasuringWorth.com <http://MeasuringWorth.com>`__

  A `data.frame` containing:

  Year
      numeric year 1947:2012

  Number.thousands
      number of families in the US

  quintile1, quintile2, median, quintile3, quintile4, p95
      quintile1, quintile2, quintile3, quintile4, and p95 are the
      indicated quantiles of the distribution of family income from US
      Census Table F-1. The media is computed as the geometric mean of
      quintile2 and quintile3. This is accurate to the extent that the
      lognormal distribution adequately approximates the central 20
      percent of the income distribution, which it should for most
      practical purposes.

  P90, P95, P99, P99.5, P99.9, P99.99
      The indicated quantiles of family income per Piketty and Saez

  realGDP.M, GDP.Deflator, PopulationK, realGDPperCap
      real GDP in millions, GDP implicit price deflators, US population in
      thousands, and real GDP per capita, according to
      `MeasuringWorth.com <http://MeasuringWorth.com>`__.

  P95IRSvsCensus
      ratio of the estimates of the 95th percentile of distributions of
      family income from the Piketty and Saez analysis of data from the
      Internal Revenue Service (IRS) and from the US Census Bureau.

      The IRS has ranged between 72 and 98 percent of the Census Bureau
      figures for the 95th percentile of the distribution, with this ratio
      averaging around 75 percent since the late 1980s. However, this
      systematic bias is modest relative to the differences between the
      different quantiles of interest in this combined dataset.

  personsPerFamily
      average number of persons per family using the number of families
      from US Census Table F-1 and the population from
      `MeasuringWorth.com <http://MeasuringWorth.com>`__.

  realGDPperFamily
      `personsPerFamily * realGDPperCap`

  mean.median
      ratio of realGDPperFamily to the median. This is a measure of
      skewness and income inequality.

  United States Census Bureau, Table F-1. Income Limits for Each Fifth and
  Top 5 Percent of Families, All Races,
http://www.census.gov/data/tables/time-series/demo/income-poverty/historical-
  income-inequality.html,
  accessed 2016-12-09.

  Thomas Piketty and Emmanuel Saez (2003) "Income Inequality in the United
  States, 1913-1998", Quarterly Journal of Economics, 118(1) 1-39,
  http://elsa.berkeley.edu/~saez, update accessed February 28, 2014.

  Louis Johnston and Samuel H. Williamson (2011) "What Was the U.S. GDP
  Then?" MeasuringWorth, http://www.measuringworth.org/usgdp, accessed
  February 28, 2014.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `income_inequality.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 66 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'income_inequality.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/incomeInequality.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='income_inequality.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
