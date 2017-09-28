# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def snow_streets(path):
  """John Snow's Map and Data on the 1854 London Cholera Outbreak

  The `Snow` data consists of the relevant 1854 London streets, the
  location of 578 deaths from cholera, and the position of 13 water pumps
  (wells) that can be used to re-create John Snow's map showing deaths
  from cholera in the area surrounding Broad Street, London in the 1854
  outbreak. Another data frame provides boundaries of a tesselation of the
  map into Thiessen (Voronoi) regions which include all cholera deaths
  nearer to a given pump than to any other.

  The apocryphal story of the significance of Snow's map is that, by
  closing the Broad Street pump (by removing its handle), Dr. Snow stopped
  the epidemic, and demonstrated that cholera is a water borne disease.
  The method of contagion of cholera was not previously understood. Snow's
  map is the most famous and classical example in the field of medical
  cartography, even if it didn't happen exactly this way. (the apocryphal
  part is that the epidemic ended when the pump handle was removed.) At
  any rate, the map, together with various statistical annotations, is
  compelling because it points to the Broad Street pump as the source of
  the outbreak.

  `Snow.deaths`: A data frame with 578 observations on the following 3
  variables, giving the address of a person who died from cholera. When
  many points are associated with a single street address, they are
  "stacked" in a line away from the street so that they are more easily
  visualized. This is how they are displayed on John Snow's original map.
  The dates of the deaths are not individually recorded in this data set.

  `case`
      Sequential case number, in some arbitrary, randomized order

  `x`
      x coordinate

  `y`
      y coordinate

  `Snow.pumps`: A data frame with 13 observations on the following 4
  variables, giving the locations of water pumps within the boundaries of
  the map.

  `pump`
      pump number

  `label`
      pump label: `Briddle St` `Broad St` ... `Warwick`

  `x`
      x coordinate

  `y`
      y coordinate

  `Snow.streets`: A data frame with 1241 observations on the following 4
  variables, giving coordinates used to draw the 528 street segment lines
  within the boundaries of the map. The map is created by drawing lines
  connecting the `n` points in each street segment.

  `street`
      street segment number: `1:528`

  `n`
      number of points in this street line segment

  `x`
      x coordinate

  `y`
      y coordinate

  `Snow.polygons`: A list of 13 data frames, giving the vertices of
  Thiessen (Voronoi) polygons containing each pump. Their boundaries
  define the area that is closest to each pump relative to all other
  pumps. They are mathematically defined by the perpendicular bisectors of
  the lines between all pumps. Each data frame contains:

  `x`
      x coordinate

  `y`
      y coordinate

  `Snow.deaths2`: An alternative version of `Snow.deaths` correcting
  some possible duplicate and missing cases, as described in
  `vignette("Snow_deaths-duplicates")`.

  `Snow.dates`: A data frame of 44 observations and 3 variables from
  Table 1 of Snow (1855), giving the number of fatal attacks and number of
  deaths by date from Aug. 19 – Sept. 30, 1854. There are a total of 616
  deaths represented in both columns `attacks` and `deaths`; of these,
  the date of the attack is unknown for 45 cases.

  Tobler, W. (1994). Snow's Cholera Map,
  `http://www.ncgia.ucsb.edu/pubs/snow/snow.html`; data files were
  obtained from `http://ncgia.ucsb.edu/Publications/Software/cholera/`,
  but these sites seem to be down.

  The data in these files were first digitized in 1992 by Rusty Dodson of
  the NCGIA, Santa Barbara, from the map included in the book by John
  Snow: "Snow on Cholera...", London, Oxford University Press, 1936.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `snow_streets.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1241 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'snow_streets.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Snow.streets.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='snow_streets.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
