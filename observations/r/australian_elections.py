# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def australian_elections(path):
  """elections to Australian House of Representatives, 1949-2007

  Aggregate data on the 24 elections to Australia's House of
  Representatives, 1949 to 2007.

  A data frame with the following variables:

  `date`
      date of election, stored using the `Date` class

  `Seats`
      numeric, number of seats in the House of Representatives

  `Uncontested`
      numeric, number of uncontested seats

  `ALPSeats`
      numeric, number of seats won by the Australian Labor Party

  `LPSeats`
      numeric, number of seats won by the Liberal Party

  `NPSeats`
      numeric, number of seats won by the National Party (previously known
      as the Country Party)

  `OtherSeats`
      numeric, number of seats won by other parties and/or independent
      candidates

  `ALP`
      numeric, percentage of first preference votes cast for Australian
      Labor Party candidates

  `ALP2PP`
      numeric, percentage of the two-party preferred vote won by
      Australian Labor Party candidates

  `LP`
      numeric, percent of first preference votes cast for Liberal Party
      candidates

  `NP`
      numeric, percent of first preference votes cast for National Party
      (Country Party) candidates

  `DLP`
      numeric, percent of first preference votes cast for Democratic Labor
      Party candidates

  `Dem`
      numeric, percent of first preference votes cast for Australian
      Democrat candidates

  `Green`
      numeric, percent of first preference votes cast for Green Party
      candidates

  `Hanson`
      numeric, percent of first preference votes cast for candidates from
      Pauline Hanson's One Nation party

  `Com`
      numeric, percent of first preference votes cast for Communist Party
      candidates

  `AP`
      numeric, percent of first preference votes cast for Australia Party
      candidates

  `Informal`
      numeric, percent of ballots cast that are spoiled, blank, or
      otherwise uncountable (usually because of errors in enumerating
      preferences)

  `Turnout`
      numeric, percent of enrolled voters recorded as having turned out to
      vote (Australia has compulsory voting)

  Australian Electoral Commission. http://www.aec.gov.au.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `australian_elections.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'australian_elections.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/AustralianElections.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='australian_elections.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
