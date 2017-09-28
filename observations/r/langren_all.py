# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def langren_all(path):
  """van Langren's Data on Longitude Distance between Toledo and Rome

  Michael Florent van Langren (1598-1675) was a Dutch mathematician and
  astronomer, who served as a royal mathematician to King Phillip IV of
  Spain, and who worked on one of the most significant problems of his
  time— the accurate determination of longitude, particularly for
  navigation at sea.

  In order to convince the Spanish court of the seriousness of the problem
  (often resulting in great losses through ship wrecks), he prepared a
  1-dimensional line graph, showing all the available estimates of the
  distance in longitude between Toledo and Rome, which showed large
  errors, for even this modest distance. This 1D line graph, from Langren
  (1644), is believed to be the first known graph of statistical data
  (Friendly etal., 2010). It provides a compelling example of the notions
  of statistical variability and bias.

  The data frame `Langren1644` gives the estimates and other information
  derived from the previously known 1644 graph. It turns out that van
  Langren produced other versions of this graph, as early as 1628. The
  data frame `Langren.all` gives the estimates derived from all known
  versions of this graph.

  `Langren1644`: A data frame with 12 observations on the following 9
  variables, giving determinations of the distance in longitude between
  Toledo and Rome, from the 1644 graph.

  `Name`
      The name of the person giving a determination, a factor with levels
      `A. Argelius` ... `T. Brahe`

  `Longitude`
      Estimated value of the longitude distance between Toledo and Rome

  `Year`
      Year associated with this determination

  `Longname`
      A longer version of the `Name`, where appropriate; a factor with
      levels `Andrea Argoli` `Christoph Clavius` `Tycho Brahe`

  `City`
      The principal city where this person worked; a factor with levels
      `Alexandria` `Amsterdam` `Bamberg` `Bologna` `Frankfurt`
      `Hven` `Leuven` `Middelburg` `Nuremberg` `Padua` `Paris`
      `Rome`

  `Country`
      The country where this person worked; a factor with levels
      `Belgium` `Denmark` `Egypt` `Flanders` `France`
      `Germany` `Italy` `Italy `

  `Latitude`
      Latitude of this `City`; a numeric vector

  `Source`
      Likely source for this determination of Longitude; a factor with
      levels `Astron` `Map`

  `Gap`
      A numeric vector indicating whether the `Longitude` value is below
      or above the median

  `Langren.all`: A data frame with 61 observations on the following 4
  variables, giving determinations of Longitude between Toledo and Rome
  from all known versions of van Langren's graph.

  `Author`
      Author of the graph, a factor with levels `Langren` `Lelewel`

  `Year`
      Year of publication

  `Name`
      The name of the person giving a determination, a factor with levels
      `Algunos1` `Algunos2` `Apianus` ... `Schonerus`

  `Longitude`
      Estimated value of the longitude distance between Toledo and Rome

  The longitude values were digitized from images of the various graphs,
  which may be found on the Supplementary materials page for Friendly
  etal. (2009).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `langren_all.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 61 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'langren_all.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Langren.all.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='langren_all.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
