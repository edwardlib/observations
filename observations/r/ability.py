from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ability(path):
  """16 ability items scored as correct or incorrect.

  16 multiple choice ability items 1525 subjects taken from the Synthetic
  Aperture Personality Assessment (SAPA) web based personality assessment
  project are saved as `iqitems`. Those data are shown as examples of
  how to score multiple choice tests and analyses of response
  alternatives. When scored correct or incorrect, the data are useful for
  demonstrations of tetrachoric based factor analysis `irt.fa` and
  finding tetrachoric correlations.

  A data frame with 1525 observations on the following 16 variables. The
  number following the name is the item number from SAPA.

  `reason.4`
      Basic reasoning questions

  `reason.16`
      Basic reasoning question

  `reason.17`
      Basic reasoning question

  `reason.19`
      Basic reasoning question

  `letter.7`
      In the following alphanumeric series, what letter comes next?

  `letter.33`
      In the following alphanumeric series, what letter comes next?

  `letter.34`
      In the following alphanumeric series, what letter comes next

  `letter.58`
      In the following alphanumeric series, what letter comes next?

  `matrix.45`
      A matrix reasoning task

  `matrix.46`
      A matrix reasoning task

  `matrix.47`
      A matrix reasoning task

  `matrix.55`
      A matrix reasoning task

  `rotate.3`
      Spatial Rotation of type 1.2

  `rotate.4`
      Spatial Rotation of type 1.2

  `rotate.6`
      Spatial Rotation of type 1.1

  `rotate.8`
      Spatial Rotation of type 2.3

  The example data set is taken from the Synthetic Aperture Personality
  Assessment personality and ability test at http://sapa-project.org. The
  data were collected with David Condon from 8/08/12 to 8/31/12.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ability.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1525 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ability.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/psych/ability.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ability.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
