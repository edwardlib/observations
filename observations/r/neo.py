# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def neo(path):
  """NEO correlation matrix from the NEO\_PI\_R manual

  The NEO.PI.R is a widely used personality test to assess 5 broad factors
  (Neuroticism, Extraversion, Openness, Agreeableness and
  Conscientiousness) with six facet scales for each factor. The
  correlation matrix of the facets is reported in the NEO.PI.R manual for
  1000 subjects.

  A data frame of a 30 x 30 correlation matrix with the following 30
  variables.

  N1
      Anxiety

  N2
      AngryHostility

   N3
      Depression

   N4
      Self-Consciousness

   N5
      Impulsiveness

   N6
      Vulnerability

   E1
      Warmth

   E2
      Gregariousness

   E3
      Assertiveness

   E4
      Activity

   E5
      Excitement-Seeking

   E6
      PositiveEmotions

   O1
      Fantasy

   O2
      Aesthetics

   O3
      Feelings

   O4
      Ideas

   O5
      Actions

   O6
      Values

   A1
      Trust

   A2
      Straightforwardness

   A3
      Altruism

   A4
      Compliance

   A5
      Modesty

   A6
      Tender-Mindedness

   C1
      Competence

   C2
      Order

   C3
      Dutifulness

   C4
      AchievementStriving

   C5
      Self-Discipline

   C6
      Deliberation

  Costa, Paul T. and McCrae, Robert R. (1992) (NEO PI-R) professional
  manual. Psychological Assessment Resources, Inc. Odessa, FL. (with
  permission of the author and the publisher)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `neo.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 30 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'neo.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/neo.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='neo.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
