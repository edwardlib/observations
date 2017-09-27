# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_tax_words(path):
  """Number of Words in US Tax Law

  Thousands of words in US tax law for 1995 to 2015 in 10 year intervals.
  This includes income taxes and all taxes in the code itself (written by
  congress) and regulations (written by government administrators). For
  2015 only "EntireTaxCodeAndRegs" is given; for other years, this number
  is broken down by income tax vs. other taxes and code vs. regulations.

  A `data.frame` containing:

  year
      tax year

  IncomeTaxCode
      number of words in thousands in the US income tax code

  otherTaxCode
      number of words in thousands in US tax code other than income tax

  EntireTaxCode
      number of words in thousands in the US tax code

  IncomeTaxRegulations
      number of words in thousands in US income tax regulations

  otherTaxRegulations
      number of words in thousands in US tax regulations other than income
      tax

  IncomeTaxCodeAndRegs
      number of words in thousands in both the code and regulations for
      the US income tax

  otherTaxCodeAndRegs
      number of wrds in thousands in both code and regulations for US
      taxes apart from income taxes.

  EntireTaxCodeAndRegs
      number of words in thousands in US tax code and regulations

  `Tax Foundation: Number of Words in Internal Revenue Code and Federal
  Tax Regulations,
1955-2005 <http://taxfoundation.org/article/number-words-internal-revenue-cod
  e-and-federal-tax-regulations-1955-2005>`__
  Scott Greenberg, `"Federal Tax Laws and Regulations are Now Over 10
  Million Words Long", October 08,
2015 <http://taxfoundation.org/blog/federal-tax-laws-and-regulations-are-now-
  over-10-million-words-long>`__

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_tax_words.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_tax_words.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/UStaxWords.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_tax_words.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
