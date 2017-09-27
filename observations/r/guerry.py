# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def guerry(path):
  """Data from A.-M. Guerry, "Essay on the Moral Statistics of France"

  Andre-Michel Guerry (1833) was the first to systematically collect and
  analyze social data on such things as crime, literacy and suicide with
  the view to determining social laws and the relations among these
  variables.

  The Guerry data frame comprises a collection of 'moral variables' on the
  86 departments of France around 1830. A few additional variables have
  been added from other sources.

  A data frame with 86 observations (the departments of France) on the
  following 23 variables.

  `dept`
      Department ID: Standard numbers for the departments, except for
      Corsica (200)

  `Region`
      Region of France ('N'='North', 'S'='South', 'E'='East', 'W'='West',
      'C'='Central'). Corsica is coded as NA

  `Department`
      Department name: Departments are named according to usage in 1830,
      but without accents. A factor with levels `Ain` `Aisne`
      `Allier` ... `Vosges` `Yonne`

  `Crime_pers`
      Population per Crime against persons. Source: A2 (Compte général,
      1825-1830)

  `Crime_prop`
      Population per Crime against property. Source: A2 (Compte général,
      1825-1830)

  `Literacy`
      Percent Read & Write: Percent of military conscripts who can read
      and write. Source: A2

  `Donations`
      Donations to the poor. Source: A2 (Bulletin des lois)

  `Infants`
      Population per illegitimate birth. Source: A2 (Bureaau des
      Longitudes, 1817-1821)

  `Suicides`
      Population per suicide. Source: A2 (Compte général, 1827-1830)

  `MainCity`
      Size of principal city ('1:Sm', '2:Med', '3:Lg'), used as a
      surrogate for poulation density. Large refers to the top 10, small
      to the bottom 10; all the rest are classed Medium. Source: A1. An
      ordered factor with levels `1:Sm` < `2:Med` < `3:Lg`

  `Wealth`
      Per capita tax on personal property. A ranked index based on taxes
      on personal and movable property per inhabitant. Source: A1

  `Commerce`
      Commerce and Industry, measured by the rank of the number of patents
      / population. Source: A1

  `Clergy`
      Distribution of clergy, measured by the rank of the number of
      Catholic priests in active service / population. Source: A1
      (Almanach officiel du clergy, 1829)

  `Crime_parents`
      Crimes against parents, measured by the rank of the ratio of crimes
      against parents to all crimes– Average for the years 1825-1830.
      Source: A1 (Compte général)

  `Infanticide`
      Infanticides per capita. A ranked ratio of number of infanticides to
      population– Average for the years 1825-1830. Source: A1 (Compte
      général)

  `Donation_clergy`
      Donations to the clergy. A ranked ratio of the number of bequests
      and donations inter vivios to population– Average for the years
      1815-1824. Source: A1 (Bull. des lois, ordunn. d'autorisation)

  `Lottery`
      Per capita wager on Royal Lottery. Ranked ratio of the proceeds bet
      on the royal lottery to population— Average for the years 1822-1826.
      Source: A1 (Compte rendus par le ministre des finances)

  `Desertion`
      Military disertion, ratio of the number of young soldiers accused of
      desertion to the force of the military contingent, minus the deficit
      produced by the insufficiency of available billets– Average of the
      years 1825-1827. Source: A1 (Compte du ministere du guerre, 1829
      etat V)

  `Instruction`
      Instruction. Ranks recorded from Guerry's map of Instruction. Note:
      this is inversely related to `Literacy` (as defined here)

  `Prostitutes`
      Prostitutes in Paris. Number of prostitutes registered in Paris from
      1816 to 1834, classified by the department of their birth Source:
      Parent-Duchatelet (1836), *De la prostitution en Paris*

  `Distance`
      Distance to Paris (km). Distance of each department centroid to the
      centroid of the Seine (Paris) Source: cakculated from department
      centroids

  `Area`
      Area (1000 km^2). Source: Angeville (1836)

  `Pop1831`
      1831 population. Population in 1831, taken from Angeville (1836),
      *Essai sur la Statistique de la Population français*, in 1000s

  Angeville, A. (1836). *Essai sur la Statistique de la Population
  française* Paris: F. Doufour.

  Guerry, A.-M. (1833). *Essai sur la statistique morale de la France*
  Paris: Crochard. English translation: Hugh P. Whitt and Victor W.
  Reinking, Lewiston, N.Y. : Edwin Mellen Press, 2002.

  Parent-Duchatelet, A. (1836). *De la prostitution dans la ville de
  Paris*, 3rd ed, 1857, p. 32, 36

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `guerry.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 86 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'guerry.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Guerry.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='guerry.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
