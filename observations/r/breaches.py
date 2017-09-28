# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def breaches(path):
  """Cyber Security Breaches

  `data.frame` of cyber security breaches involving health care records
  of 500 or more humans reported to the U.S. Department of Health and
  Human Services (HHS) as of June 27, 2014.

  A `data.frame` with 1055 observations on the following 24 variables:

  Number
      integer record number in the HHS data base

  Name\_of\_Covered\_Entity
      `factor` giving the name of the entity experiencing the breach

  State
      Factor giving the 2-letter code of the state where the breach
      occurred. This has 52 levels for the 50 states plus the District of
      Columbia (DC) and Puerto Rico (PR).

  Business\_Associate\_Involved
      Factor giving the name of a subcontractor (or blank) associated with
      the breach.

  Individuals\_Affected
      `integer` number of humans whose records were compromised in the
      breach. This is 500 or greater; U.S. law requires reports of
      breaches involving 500 or more records but not of breaches involving
      fewer.

  Date\_of\_Breach
      `character` vector giving the date or date range of the breach.
      Recodes as `Date`\ s in `breach_start` and `breach_end`.

  Type\_of\_Breach
      `factor` with 29 levels giving the type of breach (e.g., "Theft"
      vs., "Unauthorized Access/Disclosure", etc.)

  Location\_of\_Breached\_Information
      `factor` with 41 levels coding the location from which the breach
      occurred (e.g., "Paper", "Laptop", etc.)

  Date\_Posted\_or\_Updated
      `Date` the information was posted to the HHS data base or last
      updated.

  Summary
      `character` vector of a summary of the incident.

  breach\_start
      `Date` of the start of the incident = first date given in
      `Date_of_Breach` above.

  `breach_end` `Date` of the end of the incident or `NA` if only one
  date is given in `Date_of_Breach` above. `year` `integer` giving
  the year of the breach

  U.S. Department of Health and Human Services: Health Information
  Privacy: `Breaches Affecting 500 or More
  Individuals <https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf>`__

  See Also
  ~~~~~~~~

  `HHSCyberSecurityBreaches` for a version of these data downloaded more
  recently. This newer version includes changes in reporting and in the
  variables included in the `data.frame`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `breaches.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1055 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'breaches.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/breaches.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='breaches.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
