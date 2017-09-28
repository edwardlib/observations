# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def macdonell(path):
  """Macdonell's Data on Height and Finger Length of Criminals, Gosset (1908)

  In the second issue of *Biometrika*, W. R. Macdonell (1902) published an
  extensive paper, *On Criminal Anthropometry and the Identification of
  Criminals* in which he included numerous tables of physical
  characteristics 3000 non-habitual male criminals serving their sentences
  in England and Wales. His Table III (p. 216) recorded a bivariate
  frequency distribution of `height` by `finger` length. His main
  purpose was to show that Scotland Yard could have indexed their material
  more efficiently, and find a given profile more quickly.

  W. S. Gosset (aka "Student") used these data in two classic papers in
  1908, in which he derived various characteristics of the sampling
  distributions of the mean, standard deviation and Pearson's r. He said,
  "Before I had succeeded in solving my problem analytically, I had
  endeavoured to do so empirically." Among his experiments, he randomly
  shuffled the 3000 observations from Macdonell's table, and then grouped
  them into samples of size 4, 8, ..., calculating the sample means,
  standard deviations and correlations for each sample.

  `Macdonell`: A frequency data frame with 924 observations on the
  following 3 variables giving the bivariate frequency distribution of
  `height` and `finger`.

  `height`
      lower class boundaries of height, in decimal ft.

  `finger`
      length of the left middle finger, in mm.

  `frequency`
      frequency of this combination of `height` and `finger`

  `MacdonellDF`: A data frame with 3000 observations on the following 2
  variables.

  `height`
      a numeric vector

  `finger`
      a numeric vector

  Macdonell, W. R. (1902). On Criminal Anthropometry and the
  Identification of Criminals. *Biometrika*, 1(2), 177-227.
  doi:10.1093/biomet/1.2.177 http://www.jstor.org/stable/2331487

  The data used here were obtained from:

  Hanley, J. (2008). Macdonell data used by Student.
  http://www.medicine.mcgill.ca/epidemiology/hanley/Student/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `macdonell.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 924 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'macdonell.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Macdonell.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='macdonell.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
