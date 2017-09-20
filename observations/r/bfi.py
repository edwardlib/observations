from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bfi(path):
  """25 Personality items representing 5 factors

  25 personality self report items taken from the International
  Personality Item Pool (ipip.ori.org) were included as part of the
  Synthetic Aperture Personality Assessment (SAPA) web based personality
  assessment project. The data from 2800 subjects are included here as a
  demonstration set for scale construction, factor analysis, and Item
  Response Theory analysis. Three additional demographic variables (sex,
  education, and age) are also included.

  A data frame with 2800 observations on the following 28 variables. (The
  q numbers are the SAPA item numbers).

  `A1`
      Am indifferent to the feelings of others. (q\_146)

  `A2`
      Inquire about others' well-being. (q\_1162)

  `A3`
      Know how to comfort others. (q\_1206)

  `A4`
      Love children. (q\_1364)

  `A5`
      Make people feel at ease. (q\_1419)

  `C1`
      Am exacting in my work. (q\_124)

  `C2`
      Continue until everything is perfect. (q\_530)

  `C3`
      Do things according to a plan. (q\_619)

  `C4`
      Do things in a half-way manner. (q\_626)

  `C5`
      Waste my time. (q\_1949)

  `E1`
      Don't talk a lot. (q\_712)

  `E2`
      Find it difficult to approach others. (q\_901)

  `E3`
      Know how to captivate people. (q\_1205)

  `E4`
      Make friends easily. (q\_1410)

  `E5`
      Take charge. (q\_1768)

  `N1`
      Get angry easily. (q\_952)

  `N2`
      Get irritated easily. (q\_974)

  `N3`
      Have frequent mood swings. (q\_1099

  `N4`
      Often feel blue. (q\_1479)

  `N5`
      Panic easily. (q\_1505)

  `O1`
      Am full of ideas. (q\_128)

  `O2`
      Avoid difficult reading material.(q\_316)

  `O3`
      Carry the conversation to a higher level. (q\_492)

  `O4`
      Spend time reflecting on things. (q\_1738)

  `O5`
      Will not probe deeply into a subject. (q\_1964)

  `gender`
      Males = 1, Females =2

  `education`
      1 = HS, 2 = finished HS, 3 = some college, 4 = college graduate 5 =
      graduate degree

  `age`
      age in years

  Details
  ~~~~~~~

  The first 25 items are organized by five putative factors:
  Agreeableness, Conscientiousness, Extraversion, Neuroticism, and
  Opennness. The scoring key is created using `make.keys`, the scores
  are found using `score.items`.

  These five factors are a useful example of using `irt.fa` to do Item
  Response Theory based latent factor analysis of the `polychoric`
  correlation matrix. The endorsement plots for each item, as well as the
  item information functions reveal that the items differ in their
  quality.

  The item data were collected using a 6 point response scale: 1 Very
  Inaccurate 2 Moderately Inaccurate 3 Slightly Inaccurate 4 Slightly
  Accurate 5 Moderately Accurate 6 Very Accurate

  as part of the Synthetic Apeture Personality Assessment (SAPA
  http://sapa-project.org) project. To see an example of the data
  collection technique, visit http://SAPA-project.org. The items given
  were sampled from the International Personality Item Pool of Lewis
  Goldberg using the sampling technique of SAPA. This is a sample data set
  taken from the much larger SAPA data bank.

  The items are from the ipip (Goldberg, 1999). The data are from the SAPA
  project (Revelle, Wilt and Rosenthal, 2010) , collected Spring, 2010 (
  http://sapa-project.org).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bfi.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2800 rows and 28 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bfi.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/psych/bfi.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bfi.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
