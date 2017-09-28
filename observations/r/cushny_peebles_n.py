# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cushny_peebles_n(path):
  """Cushny-Peebles Data: Soporific Effects of Scopolamine Derivatives

  Cushny and Peebles (1905) studied the effects of hydrobromides related
  to scopolamine and atropine in producing sleep. The sleep of mental
  patients was measured without hypnotic (`Control`) and after treatment
  with one of three drugs: L. hyoscyamine hydrobromide
  (`L_hyoscyamine`), L. hyoscine hydrobromide (`L_hyoscyine`), and a
  mixture (racemic) form, `DL_hyoscine`, called atropine. The L (levo)
  and D (detro) form of a given molecule are optical isomers (mirror
  images).

  The drugs were given on alternate evenings, and the hours of sleep were
  compared with the intervening control night. Each of the drugs was
  tested in this manner a varying number of times in each subject. The
  average number of hours of sleep for each treatment is the response.

  Student (1908) used these data to illustrate the paired-sample t-test in
  small samples, testing the hypothesis that the mean difference between a
  given drug and the control condition was zero. This data set became well
  known when used by Fisher (1925). Both Student and Fisher had problems
  labeling the drugs correctly (see Senn & Richardson (1994)), and
  consequently came to wrong conclusions.

  But as well, the sample sizes (number of nights) for each mean differed
  widely, ranging from 3-9, and this was not taken into account in their
  analyses. To allow weighted analyses, the number of observations for
  each mean is contained in the data frame `CushnyPeeblesN`.

  `CushnyPeebles`: A data frame with 11 observations on the following 4
  variables.

  `Control`
      a numeric vector: mean hours of sleep

  `L_hyoscyamine`
      a numeric vector: mean hours of sleep

  `L_hyoscine`
      a numeric vector: mean hours of sleep

  `D_hyoscine`
      a numeric vector: mean hours of sleep

  `CushnyPeeblesN`: A data frame with 11 observations on the following 4
  variables.

  `Control`
      a numeric vector: number of observations

  `L_hyoscyamine`
      a numeric vector: number of observations

  `L_hyoscine`
      a numeric vector: number of observations

  `DL_hyoscine`
      a numeric vector: number of observations

  Cushny, A. R., and Peebles, A. R. (1905), "The Action of Optical
  Isomers. II: Hyoscines," *Journal of Physiology*, 32, 501-510.

  Senn, Stephen, Data from Cushny and Peebles,
  http://www.senns.demon.co.uk/Data/Cushny.xls

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cushny_peebles_n.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cushny_peebles_n.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/CushnyPeeblesN.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cushny_peebles_n.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
