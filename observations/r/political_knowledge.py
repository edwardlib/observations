# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def political_knowledge(path):
  """Political knowledge in the US and Europe

  Data from McChesney and Nichols (2010) on domestic and international
  knowledge in Denmark, Finland, the UK and the US among college
  graduates, people with some college, and roughly 12th grade only.

  A `data.frame` containing 12 columns and 4 rows.

  country
      a character vector of Denmark, Finland, UK, and US, being the four
      countries comparied in this data set.

  DomesticKnowledge.hs, DomesticKnowledge.sc, DomesticKnowledge.c
      percent correct answers to calibrated questions regarding knowledge
      of prominent items in domestic news in a survey of residents of the
      four countries among college graduates (ending ".c"), some college
      (".sc") and high school ("hs"). Source: McChesney and Nichols (2010,
      chapter 1, chart 8).

  InternationalKnowledge.hs, InternationalKnowledge.sc,
  InternationalKnowledge.c
      percent correct answers to calibrated questions regarding knowledge
      of prominent items in international news in a survey of residents of
      the four countries by education level as for DomesticKnowledge.
      Source: McChesney and Nichols (2010, chapter 1, chart 7).

  PoliticalKnowledge.hs, PoliticalKnowledge.sc, PoliticalKnowledge.c
      average of domestic and international knowledge

  PublicMediaPerCapita
      Per capital spending on public media in 2007 in US dollars from
      McChesney and Nichols (2010, chapter 4, chart 1)

  PublicMediaRel2US
      Spending on public media relative to the US, being
      `PublicMediaPerCapita / PublicMediaPerCapita[4]`.

  Author(s)
  ~~~~~~~~~

  Spencer Graves

  Robert W. McChesney and John Nichols (2010) *The Death and Life of
  American Journalism* (Nation Books)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `political_knowledge.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'political_knowledge.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/politicalKnowledge.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='political_knowledge.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
