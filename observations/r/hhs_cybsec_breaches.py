# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hhs_cybsec_breaches(path):
  """Cybersecurity breaches reported to the US Department of Health and Human S
  ervices

  Since October 2009 organizations in the U.S. that store data on human
  health are required to report any incident that compromises the
  confidentiality of 500 or more patients / human subjects (`45 C.F.R.
164.408 <http://www.hhs.gov/ocr/privacy/hipaa/administrative/breachnotificati
  onrule/brinstruction.html>`__)
  These reports are publicly available. `HHSCyberSecurityBreaches` was
  downloaded from `the Office for Civil Rights of the U.S. Department of
  Health and Human Services,
  2015-02-26 <https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf>`__

  A dataframe containing 1151 observations of 9 variables:

  Name.of.Covered.Entity
      A `character` vector identifying the organization involved in the
      breach.

  State
      A `factor` giving the two-letter abbreviation of the US state or
      territory where the breach occurred. This has 52 levels for the 50
      states plus the District of Columbia (DC) and Puerto Rico (PR).

  Covered.Entity.Type
      A `factor` giving the organization type of the covered entity with
      levels "Business Associate", "Health Plan", "Healthcare Clearing
      House", and "Healthcare Provider"

  Individuals.Affected
      An `integer` giving the number of humans whose records were
      compromised in the breach. This is 500 or greater; U.S. law requires
      reports of breaches involving 500 or more records but not of
      breaches involving fewer.

  Breach.Submission.Date
      Date when the breach was reported.

  Type.of.Breach
      A `factor` giving one of 29 different combinations of 7 different
      breach types, separated by ", ": "Hacking/IT Incident", "Improper
      Disposal", "Loss", "Other", "Theft", "Unauthorized
      Access/Disclosure", and "Unknown"

  Location.of.Breached.Information
      A `factor` giving one of 47 different combinations of 8 different
      location categories: "Desktop Computer", "Electronic Medical
      Record", "Email", "Laptop", "Network Server", "Other", "Other
      Portable Electronic Device", "Paper/Films"

  Business.Associate.Present
      `Logical` = (Covered.Entity.Type == "Business Associate")

  Web.Description
      A character vector giving a narrative description of the incident.

  `"Breaches Affecting 500 or More Individuals" downloaded from the Office
  for Civil Rights of the U.S. Department of Health and Human Services,
  2015-02-26 <https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf>`__

  See Also
  ~~~~~~~~

  `breaches` for an earlier download of these data. The exact reporting
  requirements and even the number and definitions of variables included
  in the `data.frame` have changed.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hhs_cybsec_breaches.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1151 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hhs_cybsec_breaches.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/HHSCyberSecurityBreaches.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hhs_cybsec_breaches.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
